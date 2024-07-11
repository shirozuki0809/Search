import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

url = 'https://example.com'
html_content = crawl(url)
if html_content:
    text_content = parse(html_content)
    print(text_content)
