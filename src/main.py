import sys
import os
import requests
import httpx
from bs4 import BeautifulSoup
from inline_html import trim_html, process_html

def main():
    url = os.getenv("BASH_URL")
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url + "/"
    with httpx.Client(http2=True, verify=False) as client:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = client.get("https://your-target-url.com", headers=headers)
        print(response.text)
        html_text = response.text
        trim_html(html_text)
    # if html_text.startswith("http://") or html_text.startswith("https://"):
    #     pass
    # else:
    #     html_text = "https://" + html_text
    # process_html(trim_html(html_text))


    # basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    # need to update this function to go the other way. Hopefully recurse through all pages?
    # generate_pages_recursive("content", "template.html", "docs", basepath)

main()