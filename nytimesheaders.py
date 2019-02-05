
#!/usr/bin/env python3
# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
headings = soup.findAll("h2", {"class": "story-heading"})

for heading in headings:
    if heading.findAll("a"):
        # .strip() removes leading/trailing whitespace
        print(heading.a.text.strip())
    else:
        print(heading.text)