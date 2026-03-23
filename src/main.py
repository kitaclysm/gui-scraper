import sys
import os
from bs4 import BeautifulSoup
from inline_html import get_fully_rendered_html, process_html

def main():
    url = os.getenv("BASH_URL")
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url + "/"
    print(get_fully_rendered_html(url))

    # if html_text.startswith("http://") or html_text.startswith("https://"):
    #     pass
    # else:
    #     html_text = "https://" + html_text
    # process_html(trim_html(html_text))


    # basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    # need to update this function to go the other way. Hopefully recurse through all pages?
    # generate_pages_recursive("content", "template.html", "docs", basepath)

main()