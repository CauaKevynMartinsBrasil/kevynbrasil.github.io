# Caua Kevyn Martins Brasil — Portfolio

A responsive, multi-page finance portfolio with dedicated About, Projects, Experience, Highlights, Résumé, and Contact pages, plus three detailed work stories. The site uses plain HTML and CSS and has no external dependencies.

## Publish on GitHub Pages

1. Keep all generated `.html` pages, `site.css`, and `.nojekyll` at the root of this repository's `main` branch.
2. Open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then **main** and **/ (root)**. Save.
3. GitHub displays the live address on the Pages settings page once deployment finishes. Under the current account, the project-site address is `https://cauakevynmartinsbrasil.github.io/kevynbrasil.github.io/`.

For the shorter address `https://kevynbrasil.github.io/`, the GitHub account username must also be `kevynbrasil`. The name displayed on the portfolio is independent of the URL.

Official setup guide: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Edit

Edit `build_site.py` for copy and page structure, or `site.css` for styling. Run `python3 build_site.py` to regenerate the HTML pages, then review `index.html` in a browser. Relative links keep the site working under either a personal or project GitHub Pages URL.
