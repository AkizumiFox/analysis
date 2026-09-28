# Deploying to GitHub Pages (content only, no build scripts)

This setup deploys only the built site (HTML, section PDFs, full book) to a **single public repo** that has no build scripts.

## One-time setup

1. Create a **new empty public repo** on GitHub (e.g. `my-book`).

2. Set the deploy URL in `config/config.json`:
   ```json
   "deploy-repo": "https://github.com/YOUR_USERNAME/YOUR_REPO.git"
   ```

3. Run deploy (clones the repo into `site/` on first run):
   ```bash
   python build.py deploy --push
   ```

4. In GitHub repo **Settings > Pages**: Set source to **Deploy from a branch**, branch **main**, folder **/ (root)**.

5. **Custom domain** (optional): In `config/config.json`, add:
   ```json
   "deploy-domain": "my-book.example.com"
   ```
   The deploy adds a `CNAME` file so GitHub Pages serves at your domain. In **Settings > Pages**, enter the custom domain and follow GitHub's DNS instructions (CNAME record or A records).

## Deploy workflow

```bash
python build.py deploy --push
```

`deploy` builds everything and runs `./build.py check` first; it copies nothing if either fails.
To push somewhere other than the clone's `origin` (for example over SSH when the HTTPS remote
has no stored credentials), set `"deploy-push-url"` in `config/config.json`.

Or split into steps:
```bash
python build.py deploy          # Build and copy to site/
cd site && git add -A && git commit -m "Deploy" && git push
```

## Result

- **Public repo** contains only: `index.html`, `styles.css`, `main.js`, chapter folders, `pdf/`, `book/`, search/navigation JSON, and `labels.json` (the label registry other books cite this one through).
- **No** `build/`, `src/`, `templates/`, or config in the public repo.
- GitHub Pages serves the site from the root.

## Several books under one origin (a library)

Books built with this engine can share one site, each under its own path:

```
books.example.com/
├── index.html            the library's own page (below)
├── 404.html              optional: GitHub Pages serves only the root one
├── CNAME                 books.example.com
├── analysis/             ./build.py deploy output of the analysis book
├── linear-algebra/       … of the linear-algebra book
└── regression/           … of the regression book
```

Every link and asset a book writes is relative, so a built `_build/html` works unchanged at
any path. Two settings make the rest right:

1. In each book's config, set `site-url` to its address and leave `deploy-domain` empty (the
   library repository carries the one `CNAME`):
   ```json
   "site-url": "https://books.example.com/analysis/",
   "deploy-domain": ""
   ```
   Canonical links, `sitemap.xml` and the PDF's links to runnable cells use it, and the
   book's `404.html` links to `/analysis/`. No `robots.txt` is written for a sub-path; put
   one at the library root if wanted.
2. Point cross-book references at the sibling path, so links and hover previews stay on
   the same origin:
   ```json
   "external-books": {
     "la": { "title": "Linear Algebra", "short": "LA", "url": "../linear-algebra/",
             "labels": "../linear-algebra/_build/crossref_labels.json" }
   }
   ```
   `labels` can also be the deployed registry, `https://books.example.com/linear-algebra/labels.json`.

To publish, make one library repository (GitHub Pages, branch `main`, folder `/`) and copy
each book's output into its directory, e.g. with `"deploy-dir": "../library/analysis"` in each
book's config and `./build.py deploy` (without `--push`; commit and push the library once).
The deploy empties `deploy-dir` except `.git`, so give each book its own subdirectory, never
the library root.

A minimal `index.html` for the library root:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Books</title>
  <link rel="stylesheet" href="analysis/styles.css">
</head>
<body>
  <main class="not-found">
    <h1>Books</h1>
    <ul>
      <li><a href="analysis/">Analysis: From First Proofs to Modern Analysis</a></li>
      <li><a href="linear-algebra/">Linear Algebra</a></li>
      <li><a href="regression/">Regression</a></li>
    </ul>
  </main>
</body>
</html>
```

A book can also stay on its own domain and still be cited: use its absolute `url`. Previews
then come from another origin, which works when that site allows cross-origin reads (GitHub
Pages does) and otherwise leaves a plain link.
