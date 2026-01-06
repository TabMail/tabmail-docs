# TabMail Docs — content guide

## Goals

- Be **user-facing**: focus on “what to do”, not internal architecture.
- Be **Thunderbird v145+ accurate**.
- Prefer **short, concrete steps** and **copy/paste-ready** wording.
- If something is unclear, document the **expected behavior** and add a “Known issue / TODO” line instead of guessing.

## Writing style

- Use short sections (`##`, `###`)
- Prefer bullet lists and numbered steps
- Use blockquotes for notes and caveats
- Avoid deep nesting

## Markdown renderer limitations

Docs use TabMail’s minimal markdown renderer (`https://tabmail.ai/js/md-page.js`).

Supported:

- Headings `#` through `######`
- Paragraphs
- Lists (`-`, `1.`)
- Blockquotes (`>`)
- Fenced code blocks (```)
- Horizontal rules (`---`)
- Pipe tables

Avoid:

- Raw HTML (only a tiny allowlist is supported)
- Complex GitHub-flavored markdown extensions


