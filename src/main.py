import sys
import os

def main():
    url = os.getenv("BASH_URL")
    
    # basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    # need to update this function to go the other way. Hopefully recurse through all pages?
    # generate_pages_recursive("content", "template.html", "docs", basepath)

main()