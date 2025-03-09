import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
print(html.decode())
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
