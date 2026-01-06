# TabMail Docs

User-facing documentation for **TabMail** (Thunderbird **v145+**).

- Live site: `https://docs.tabmail.ai/`
- Product site: `https://tabmail.ai/`

## Support / help tickets

This repo is also the **public support tracker**.

- Open an issue: `https://github.com/TabMail/tabmail-docs/issues/new/choose`

We use GitHub issue forms (Bug report / Feature request / Support question / Docs issue) to keep reports structured.

## Repo structure

This is a simple static site:

- `web/`: Cloudflare Pages output directory
  - `index.html` + `index.md`: docs homepage
  - `<slug>/index.html` + `<slug>/index.md`: a docs page
  - `_redirects`: Cloudflare Pages redirects (canonical trailing slash, assets redirect)
- `run_local_server.py`: local server for testing (clean URLs)
- `MAINTENANCE.md`: maintainability notes (how to add pages)
- `CONTENT_GUIDE.md`: writing guide + markdown renderer constraints

## Local development

Run the local server:

```bash
cd /Users/kwang/Work/GitData/tabmail/tabmail-docs
python3 run_local_server.py
```

Then open `http://localhost:8001/`.

Notes:
- `/faq` redirects to `/faq/` locally (matches Cloudflare Pages).
- `/assets/*` redirects to `https://tabmail.ai/assets/*` so shared scripts work.

## Deployment (Cloudflare Pages)

This site is designed for **no-build** deployment.

Recommended settings:

- **Framework preset**: None
- **Build command**: (empty)
- **Output directory**: `web`

Cloudflare Pages deploys on every push to the default branch.

## Shared theme + scripts

To keep the docs site visually consistent with `tabmail.ai`, docs pages load shared assets from `tabmail.ai`:

- CSS: `https://tabmail.ai/css/*`
- JS: `https://tabmail.ai/js/header.js`, `footer.js`, `md-page.js`, `favicon-theme.js`

Some shared scripts reference site-relative `/assets/*`; this repo supports that via an `_redirects` rule that forwards `docs.tabmail.ai/assets/*` to `tabmail.ai/assets/*`.


