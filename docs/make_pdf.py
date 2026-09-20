#!/usr/bin/env python3
"""THECC Academy — render the brand-styled HTML to PDF with the standard running footer.

Usage:  python3 make_pdf.py [FILE.md ...]     (no args = every .md in this folder)
Requires: playwright (pip install playwright) and the bundled Chromium at
PLAYWRIGHT_BROWSERS_PATH, plus render.py for the markdown -> HTML step.
"""
import pathlib, re, subprocess, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
# The session ships Chromium at PLAYWRIGHT_BROWSERS_PATH; never run "playwright install".
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FOOTER = (
    "<div style=\"width:100%;font-family:'Segoe UI',Arial,sans-serif;font-size:8px;"
    "color:#9AA3B2;padding:0 14mm;display:flex;justify-content:space-between\">"
    "<span>THECC Institutional Trader Academy™ · {title} · © THE CONSISTENCY COLLECTIVE</span>"
    "<span>Page <span class='pageNumber'></span> of <span class='totalPages'></span></span></div>"
)

def title_of(html_path):
    m = re.search(r"<title>(.*?)</title>", html_path.read_text(encoding="utf-8"), re.S)
    return (m.group(1) if m else html_path.stem).replace("&amp;", "&")

def main(argv):
    subprocess.run([sys.executable, str(HERE / "render.py")], check=True, cwd=HERE,
                   stdout=subprocess.DEVNULL)
    targets = [HERE / a for a in argv] if argv else sorted(HERE.glob("*.md"))
    htmls = [t.with_suffix(".html") for t in targets]
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page()
        for html in htmls:
            if not html.exists():
                print(f"skip (no html): {html.name}")
                continue
            pdf = html.with_suffix(".pdf")
            page.goto(html.as_uri(), wait_until="load")
            page.pdf(path=str(pdf), format="A4", print_background=True,
                     display_header_footer=True, header_template="<div></div>",
                     footer_template=FOOTER.format(title=title_of(html)),
                     margin={"top": "14mm", "bottom": "16mm", "left": "0mm", "right": "0mm"})
            print(f"{pdf.name:58} {pdf.stat().st_size:>8} bytes")
        browser.close()

if __name__ == "__main__":
    main(sys.argv[1:])
