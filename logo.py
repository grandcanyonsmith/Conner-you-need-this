import requests
from bs4 import BeautifulSoup

def print_image_urls(page_url):
    response = requests.get(page_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        if images:
            for img in images:
                img_url = img.get('src', '')
                if img_url:
                    print(img_url)
        else:
            print("No images found on the webpage.")
    else:
        print(f"Error fetching the webpage: HTTP {response.status_code}")

if __name__ == '__main__':
    page_url = 'https://coursecreator360.com/'
    print_image_urls(page_url)