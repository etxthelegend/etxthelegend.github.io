"""Build the site: reads src/content.yml + src/templates/ + src/static/ and writes the
published HTML into the repository root (GitHub Pages serves it from there).

    pip install pyyaml jinja2
    python build.py
"""
import datetime, pathlib, shutil, yaml
from jinja2 import Environment, FileSystemLoader

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent

NAV = [("home", "Home", "index.html"), ("research", "Research", "research.html"),
       ("projects", "Projects", "projects.html"), ("publications", "Publications", "publications.html")]
CATEGORIES = {"research": "Research", "design": "Design & build", "analysis": "Analysis", "personal": "Personal"}

data = yaml.safe_load((ROOT / "content.yml").read_text(encoding="utf-8"))
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
base = dict(data, nav=NAV, categories=CATEGORIES, year=datetime.date.today().year)


def render(template, out, root="", **extra):
    path = OUT / out
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(env.get_template(template).render(**base, root=root, **extra), encoding="utf-8")


# clear previously generated output (never touches src/ or .github/)
for f in OUT.glob("*.html"):
    f.unlink()
for d in ("projects", "files", "img"):
    if (OUT / d).exists():
        shutil.rmtree(OUT / d)
for folder in ("static", "img", "files"):
    src = ROOT / folder
    if src.exists():
        shutil.copytree(src, OUT if folder == "static" else OUT / folder, dirs_exist_ok=True)
(OUT / ".nojekyll").touch()

render("index.html", "index.html", active="home")
render("research.html", "research.html", active="research", page_title="Research")
render("projects.html", "projects.html", active="projects", page_title="Projects")
render("publications.html", "publications.html", active="publications", page_title="Publications")
render("cv.html", "cv.html", active="cv", page_title="CV")

projects = data["projects"]
for i, p in enumerate(projects):
    render("project.html", f"projects/{p['slug']}.html", root="../", active="projects",
           page_title=p["title"], description=p["summary"], p=p,
           prev=projects[i - 1] if i > 0 else None,
           next=projects[i + 1] if i + 1 < len(projects) else None)

print(f"Built {5 + len(projects)} pages into {OUT}")
