from html.parser import HTMLParser
import re
import requests
from googlesearch import search
import lxml
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data): 
        self.text.append(data)

def remove_tags(html):
 
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
 
def get_clean_html(url):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        # Remove extra whitespace and newlines
        cleaned_html = re.sub(r'\s+', ' ', html)
        return cleaned_html
    except requests.exceptions.RequestException as e:
        print("Error fetching HTML:", e)
        return None


def google_search(query):
    result = search(query, num=1, stop=1, pause=2)
    if result:
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            return get_clean_html(j)
    else:
        return None
    
def get_data(query):
    html = google_search(query)
    if html:
        return remove_tags(html)
    else:
        return None

