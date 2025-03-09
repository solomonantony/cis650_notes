import requests
from bs4 import BeautifulSoup
#url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
url = 'http://python.org/'
# get the page of interest from the web
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
links = soup.find_all('a')
for link in links:
  print(link)
  # provide the page's content to Beautiful Soup, for it to parse

#print(soup.prettify())
#use find_all to find tags
soup.find_all('span')[0]
# display the title of page
#print(soup.title.text.strip())
for link in soup.find_all('a'):
  #print(link['href'])
  print(link.string, link['href'])
  #print(link.get('href'))
  
