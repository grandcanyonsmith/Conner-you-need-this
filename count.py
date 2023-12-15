from bs4 import BeautifulSoup
import re

def count_js_functions(html_content):
    # Define a regular expression pattern to find JavaScript functions
    js_function_pattern = re.compile(r'function\s+(\w+)\s*\(.*?\)\s*\{', re.MULTILINE)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all script tags
    script_tags = soup.find_all('script')

    # Counter for functions
    function_count = 0

    # Search for functions in each script tag
    for script in script_tags:
        if script.string:  # This checks if the script tag contains any content
            functions = js_function_pattern.findall(script.string)
            function_count += len(functions)

    return function_count

# Read the HTML file
with open('hello.html', 'r') as file:
    html_content = file.read()

# Count the number of JavaScript functions
num_functions = count_js_functions(html_content)

# Print the result
print(f'The file contains {num_functions} JavaScript function(s).')