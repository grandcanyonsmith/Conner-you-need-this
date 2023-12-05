import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import re

# Function to send an HTTP request and return the response content
def get_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Function to extract text from HTML content using BeautifulSoup
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

# Function to count the frequency of each word in the text
def count_word_frequencies(text):
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return word_counts

# Function to create a pandas DataFrame from word counts
def create_dataframe_from_counts(word_counts):
    df = pd.DataFrame(word_counts.most_common(), columns=['Word', 'Frequency'])
    return df

# Main script execution
if __name__ == "__main__":
    try:
        # URL of the website to analyze
        url = 'https://www.apple.com'

        # Get the content of the webpage
        content = get_webpage_content(url)

        # Extract text from the HTML content
        extracted_text = extract_text_from_html(content)

        # Count the frequencies of each word in the text
        word_frequencies = count_word_frequencies(extracted_text)

        # Create a DataFrame from the word frequencies
        df_word_frequencies = create_dataframe_from_counts(word_frequencies)

        # Print the DataFrame without truncating, to show all rows and columns
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df_word_frequencies)  # This will print the entire DataFrame to the console

    except Exception as e:
        # Print the error message to the standard error stream
        print(str(e), file=sys.stderr)