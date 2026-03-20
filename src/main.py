import sys
import os
import requests
from bs4 import BeautifulSoup
from inline_html import trim_html

def main():
    url = os.getenv("BASH_URL")
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url
    response = requests.get(url)
    html_text = response.text
    # if html_text.startswith("http://") or html_text.startswith("https://"):
    #     pass
    # else:
    #     html_text = "https://" + html_text
    trim_html(html_text)
    # basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    # need to update this function to go the other way. Hopefully recurse through all pages?
    # generate_pages_recursive("content", "template.html", "docs", basepath)

main()