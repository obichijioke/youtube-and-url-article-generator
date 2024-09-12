import requests
from bs4 import BeautifulSoup

def scrape_blog(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This is a simple implementation. You may need to adjust it based on the blog's structure
    content = soup.find('article') or soup.find('div', class_='content')
    
    if content:
        return content.get_text()
    else:
        return "Failed to extract blog content"