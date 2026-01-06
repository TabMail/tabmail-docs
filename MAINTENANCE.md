# TabMail Docs — maintenance notes

This repo is intended to be **easy to maintain** and **deployable via Cloudflare Pages** with no build step.

## How docs pages work

- Each docs page is a folder under `web/` with:
  - `index.html` (layout + shared TabMail header/footer + markdown loader)
  - `index.md` (the actual content)
- Markdown is rendered client-side using TabMail’s existing renderer (`https://tabmail.ai/js/md-page.js`).

## Adding a new doc page

1. Create a folder: `web/<slug>/`
2. Add:
   - `web/<slug>/index.html` (copy from an existing doc page)
   - `web/<slug>/index.md`
3. Add a redirect rule (optional but recommended) to `web/_redirects`:
   - `/<slug> /<slug>/ 301`
4. Add a link on the docs homepage (`web/index.md`).

## Local testing

Run the local server (clean URLs + trailing-slash redirects):

```bash
cd /Users/kwang/Work/GitData/tabmail/tabmail-docs
python3 run_local_server.py
```

Then open `http://localhost:8001/`.

## Shared theme + header/footer

We load the shared website assets from `tabmail.ai`:

- CSS: `https://tabmail.ai/css/*`
- JS: `https://tabmail.ai/js/header.js`, `footer.js`, `md-page.js`, `favicon-theme.js`

Because `header.js` references `/assets/logo-with-text*.svg`, this repo also ships matching assets under `web/assets/`.


