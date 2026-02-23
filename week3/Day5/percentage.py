import os
import webbrowser
import argparse
from textwrap import dedent

PRESETS = {
    'classic': '25,50,25',
    '20-60-20': '20,60,20',
    'thirds': '33.3333,33.3333,33.3333',
    'halves': '50,50',
    'four': '25,25,25,25'
}
def parse_layout(s: str):
    s = s.strip()
    if s in PRESETS:
        s = PRESETS[s]
    # accept both commas and hyphens
    parts = [p for p in (s.replace('-', ',').split(',')) if p]
    try:
        vals = [float(p) for p in parts]
    except ValueError:
        raise ValueError('Layout must be numbers like "25,50,25" or a preset name')
    return vals

def build_css(percentages, breakpoint):
    base = dedent('''
    *{box-sizing:border-box}
    body{font-family:Segoe UI,Arial,Helvetica,sans-serif;margin:0;background:#f2f4f6}
    .container{width:95%;max-width:1100px;margin:18px auto;background:#fff;padding:16px;border-radius:6px}
    .header{background:#0b79d0;color:#fff;padding:14px;border-radius:6px;font-size:1.2rem}
    .lead{color:#444;margin:12px 0}
    .row{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px}
    .col{background:#fafafa;padding:12px;border:1px solid #e1e4e8;border-radius:4px}
    ''')
    for i, p in enumerate(percentages, start=1):
        base += f'.col-{i}{{flex:0 0 {p}%}}\n'

    base += '\n'
    base += f'@media (max-width:{breakpoint}px){{\n'
    selector = ','.join([f'.col-{i}' for i in range(1, len(percentages) + 1)])
    base += f'  {selector}{{flex:0 0 100%}}\n}}\n'

    base += dedent('''
    @media (max-width:400px){
      .header{font-size:1rem;padding:10px}
    }
    ''')
    return base

def build_html(percentages):
    cols_html = ''
    for i, p in enumerate(percentages, start=1):
        cols_html += f'      <div class="col col-{i}"><h3>Column {i}</h3><p>{p}% width</p></div>\n'

    html = f"""<!doctype html>
<html lang=\"en\"> 
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Responsive Percentage Demo</title>
  <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
  <div class=\"container\">
    <header class=\"header\">Responsive Percentage Width Demo</header>
    <p class=\"lead\">This demo uses percentage widths and a media query to stack columns on small screens.</p>
    <section class=\"row\">\n{cols_html}    </section>
  </div>
</body>
</html>"""
    return html

def write_files(target_dir: str, percentages, breakpoint):
    html_path = os.path.join(target_dir, 'responsive.html')
    css_path = os.path.join(target_dir, 'style.css')
    with open(html_path, 'w', encoding='utf-8') as fh:
        fh.write(build_html(percentages))
    with open(css_path, 'w', encoding='utf-8') as fc:
        fc.write(build_css(percentages, breakpoint))
    return html_path, css_path

def open_file(path: str) -> None:
    try:
        webbrowser.open('file://' + os.path.abspath(path).replace('\\', '/'))
    except Exception:
        try:
            os.startfile(path)
        except Exception:
            print('Could not open file automatically:', path)

def main():
    parser = argparse.ArgumentParser(description='Generate responsive.html and style.css with percentage columns')
    parser.add_argument('--layout', '-l', default='classic', help='Layout preset or comma-separated percentages (e.g. 25,50,25)')
    parser.add_argument('--breakpoint', '-b', type=int, default=700, help='Mobile breakpoint in px')
    parser.add_argument('--open', action='store_true', help='Open responsive.html after creating')
    args = parser.parse_args()
    try:
        percentages = parse_layout(args.layout)
    except ValueError as e:
        print('Error parsing layout:', e)
        return
    base = os.path.dirname(__file__)
    html_path, css_path = write_files(base, percentages, args.breakpoint)
    print('Wrote', html_path)
    print('Wrote', css_path)
    if args.open:
        open_file(html_path)

if __name__ == '__main__':
    main()
			def main():