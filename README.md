# IY SECURITY Website

Static GitHub Pages website for https://iysecurity.com/

## Publishing research

1. Add a new HTML report under `research/`.
2. Add the recommended `iy-*` metadata to the report.
3. Commit and push to `main`.
4. GitHub Actions regenerates `research/index.json`.
5. The homepage reads the generated index and displays the new report.

## HTTPS

All first-party URLs use HTTPS. The website does not need a special HTML metadata tag to enable GitHub Pages HTTPS. In GitHub:
`Settings → Pages → Custom domain → iysecurity.com → Enforce HTTPS`.

External CSS/JS assets in the current site are already referenced using HTTPS.
