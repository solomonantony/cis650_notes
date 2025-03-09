filename = 'CDRates.html'
f = open(filename, 'r') #create a file handle
contents = f.read() #read the file and store the contents to a variable

from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, 'html.parser') #create a soup object with the contents
print(soup.title.text) # we ready to read part of the soup object
#print(soup) #it is text
print("====")
#print(soup.prettify()) #prettify makes the lines indented

span_element = soup.find('span') #find the first tag type
if span_element != None:
  print('Span element text:', span_element.text)  #most tags has a text property
span_next_element = span_element.find_next('span') #in referenced to current tag, find the next one
if span_next_element != None:
  print('Next span element text:', span_next_element.text)
  print("====")
table_rows = soup.find_all('tr')
print(type(table_rows))
for row in table_rows:
  print(row.text)
print("====")
#===  Search for a tag with its id
output1 = soup.find('span', {'id':'asofdatetime'})
print(output1)
output2 = spanElements = soup.find_all('span')
print(output2)
