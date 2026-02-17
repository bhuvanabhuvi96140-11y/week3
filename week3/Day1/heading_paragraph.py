html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple web page created using Python.</p>
    <img src="https://via.placeholder.com/150" alt="Sample Image">
    <br><br>
    <a href="https://www.google.com">Click here to visit Google</a>
</body>
</html>
"""
with open("webpage.html", "w") as file:
    file.write(html_content)
print("Web page created successfully! Open 'webpage.html' in your browser.")