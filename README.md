# etxthelegend.github.io

Personal research portfolio for Ethan Xiong.

## Editing

All text, projects, publications and CV entries live in **`src/content.yml`**. Edit it, commit, push — GitHub rebuilds and publishes the site in about a minute.

| To change… | Edit |
|---|---|
| Any text, project, paper, news item | `src/content.yml` |
| Photos and figures | drop them in `src/img/`, reference as `img/name.jpg` in `src/content.yml` |
| CV PDF | replace `src/files/Ethan_Xiong_CV.pdf` |
| Colours / fonts | `src/static/style.css` (top of file) |
| Page layout | `src/templates/*.html` |

### Adding a project
Copy an existing entry under `projects:` in `src/content.yml`, give it a new `slug`, and fill it in. Its page appears at `projects/<slug>.html` automatically. Set `featured: true` to show it on the home page.

## Previewing locally (optional)

```bash
pip install pyyaml jinja2
python src/build.py    # writes the HTML into the repo root
```
Open `index.html` in a browser. (You don't have to do this — GitHub rebuilds automatically when anything in `src/` changes.)

## Hosting
The built pages sit at the repo root and GitHub Pages serves them from the `main` branch.
The `.github/workflows/build.yml` action rebuilds them whenever `src/` changes.
