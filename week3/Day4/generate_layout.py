"""
Simple Python program to generate an HTML layout file containing a header,
navbar, content area and footer. Each section uses a `div` and applies CSS box
model concepts (margin, border, padding) via a shared `.box` class.

Running this script will overwrite `layout.html` in the same directory.
"""

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Model Layout</title>
    <style>
        /* basic reset */
        * {
            box-sizing: border-box; /* include padding/border in width/height */
        }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .box {
            margin: 10px;
            padding: 15px;
            border: 2px solid #333;
        }
        .header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
        }
        .navbar {
            background-color: #333;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        .navbar a:hover {
            background-color: #575757;
        }
        .content {
            background-color: #f9f9f9;
        }
        .footer {
            background-color: #ddd;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header box">
        <h1>Header Section</h1>
    </div>
    <div class="navbar box">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Services</a>
        <a href="#">Contact</a>
    </div>
    <div class="content box">
        <h2>Main Content</h2>
        <p>This is the content area. Notice how the .box class adds margin, padding,
        and a border around each section to illustrate the CSS box model.</p>
    </div>
    <div class="footer box">
        <p>Footer © 2026</p>
    </div>
</body>
</html>"""

if __name__ == '__main__':
    with open('layout.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('layout.html generated successfully.')
