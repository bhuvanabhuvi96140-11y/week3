html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>List Example</title>
</head>
<body>
    <h1>HTML Lists Example</h1>
    <h2>Ordered List</h2>
    <ol>
        <li>Python</li>
        <li>Java</li>
        <li>C++</li>
        <li>JavaScript</li>
    </ol>
    <h2>Unordered List</h2>
    <ul>
        <li>Apple</li>
        <li>Banana</li>
        <li>Mango</li>
        <li>Orange</li>
    </ul>
</body>
</html>
"""
with open("listpage.html", "w") as file:
    file.write(html_content)
print("HTML page with lists created successfully!")