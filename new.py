def write_script_to_html_file(filename: str, script_content: str):
    """
    Write HTML content including a script to a file with the given filename.

    Parameters:
    filename (str): The name of the HTML file where the content will be written.
    script_content (str): The JavaScript content that will be written inside the HTML file.
    """
    # Ensure the filename provided ends with a .html extension
    if not filename.endswith('.html'):
        filename += '.html'

    # Define the basic HTML structure with the provided JavaScript content
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript in HTML</title>
</head>
<body>
    <script>
    {script_content}
    </script>
</body>
</html>"""

    # Write the content to an HTML file with the given filename
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# JavaScript content to be inserted in the HTML script tag
javascript_content = """function printHelloWorld() {
  console.log("Hello, World!");
}

printHelloWorld();"""

# File name for the HTML
script_name = "hello.html"

# Function call to write the JavaScript content within an HTML file
write_script_to_html_file(script_name, javascript_content)

print(f"The script has been written to {script_name}")