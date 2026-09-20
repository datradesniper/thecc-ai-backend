import markdown, re, pathlib

CSS = """:root{--navy:#0A1428;--green:#05FF9B;--green2:#059f6b;--silver:#9AA3B2;--ink:#1a1f2b;--line:#dde3ec;}
*{box-sizing:border-box}
body{font-family:'Segoe UI',Arial,Helvetica,sans-serif;color:var(--ink);line-height:1.55;max-width:920px;margin:0 auto;padding:48px 40px;background:#fff}
h1{color:var(--navy);border-bottom:4px solid var(--green2);padding-bottom:.3em;font-size:2em;margin-top:0}
h2{color:var(--navy);border-bottom:1px solid var(--line);padding-bottom:.2em;margin-top:1.8em}
h3{color:var(--green2);margin-top:1.4em}
h4{color:var(--navy)}
a{color:var(--green2)}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.95em}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--navy);color:#fff}
tr:nth-child(even) td{background:#f6f8fb}
code{background:#f2f4f8;padding:2px 5px;border-radius:4px;font-family:Consolas,monospace;font-size:.92em}
pre{background:#0A1428;color:#d7f7ea;padding:14px 16px;border-radius:8px;overflow-x:auto;line-height:1.4}
pre code{background:none;color:inherit;padding:0}
blockquote{border-left:4px solid var(--green2);background:#f3fbf7;margin:1em 0;padding:.6em 1em;border-radius:0 6px 6px 0}
hr{border:none;border-top:2px solid var(--line);margin:2em 0}
.brandbar{background:var(--navy);color:#fff;padding:14px 20px;border-radius:8px;margin-bottom:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap}
.brandbar b{color:var(--green)}
.foot{margin-top:3em;padding-top:1em;border-top:1px solid var(--line);color:var(--silver);font-size:.85em}
@media print{body{padding:0}.brandbar{-webkit-print-color-adjust:exact;print-color-adjust:exact}th{-webkit-print-color-adjust:exact;print-color-adjust:exact}}"""

def render(md_path, title, doc_id, version):
    src = pathlib.Path(md_path).read_text(encoding='utf-8')
    body = markdown.markdown(src, extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])
    # compact: collapse the one-tag-per-line output, keeping <pre> blocks intact
    pres = []
    def stash(m):
        pres.append(m.group(0)); return f'@@PRE{len(pres)-1}@@'
    body = re.sub(r'<pre>.*?</pre>', stash, body, flags=re.S)
    body = re.sub(r'>\s*\n\s*<', '><', body)
    body = re.sub(r'\n{2,}', '\n', body)
    for i, blk in enumerate(pres):
        body = body.replace(f'@@PRE{i}@@', blk)
    html = f"""<!doctype html><html lang='en'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>{title}</title><style>
{CSS}
</style></head><body>
<div class='brandbar'><span>THECC Institutional Trader Academy™</span><span><b>Consistency Creates Freedom.</b></span></div>
{body}
<div class='foot'>THECC Institutional Trader Academy™ · {title} {version} · {doc_id} · © THE CONSISTENCY COLLECTIVE · Academy Documentation Standard v1.0</div>
</body></html>"""
    out = md_path.replace('.md', '.html')
    pathlib.Path(out).write_text(html, encoding='utf-8')
    print('wrote', out, len(html), 'bytes')


def title_and_id(src):
    """Pull the document title from the first H1 and the ID from the control table."""
    h1 = re.search(r'^# (.+)$', src, re.M)
    did = re.search(r'\| Document ID \| ([A-Z0-9-]+) \|', src)
    return (h1.group(1).strip() if h1 else 'THECC Academy Document',
            did.group(1).strip() if did else '')


def main():
    for md in sorted(pathlib.Path(__file__).parent.glob('*.md')):
        src = md.read_text(encoding='utf-8')
        title, doc_id = title_and_id(src)
        render(str(md), title, doc_id, 'v2.1.0')


if __name__ == '__main__':
    main()
