#using pandas read_html
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
import urllib.request
with urllib.request.urlopen(url) as response:
   page = response.read().decode()
dfs = pd.read_html(page)
print(len(dfs))
dfs[0].to_csv('sp500-b.csv')
print(dfs[0])

soup = BeautifulSoup(page, 'html.parser')

results = soup.find_all('table')


column_count = len(results[0].find_all('tr')[0].find_all('th'))
row_count = len(results[0].find_all('tr'))
print(row_count)
column_names = []
for column_number in range(len(results[0].find_all('th'))):
  column_names.append(results[0].find_all('th')[column_number].text.strip())

row_number = 0
table_data_frame = pd.DataFrame(columns = column_names)

for row in results[0].find_all('tr'):
  temp_data_frame = pd.DataFrame(columns = column_names)
  temp_data_list = []
  column_number = 0
  for column in row.find_all('td'):
    column_name = column_names[column_number]
    cell_data = column.text.strip()

    temp_data_list.append(cell_data)
    column_number += 1
  if (len(temp_data_list) == column_count):
    temp_data_frame = pd.DataFrame([temp_data_list], columns = column_names)
    table_data_frame = pd.concat([table_data_frame, temp_data_frame], axis=0)
    row_number += 1
print(table_data_frame)
table_data_frame.to_csv('sp500.csv')
print('Done writing to sp500.csv')

import csv
names=['Institution name','In state MBA tuition','     Yang Chen']
with open('Financial.csv', 'w', newline ='') as csvOutFile:
    writer = csv.DictWriter(csvOutFile, fieldnames = names)
    writer.writeheader()
    for i in record:
        csvOutFile.write(str(i)[1:len(str(i))-1])
        csvOutFile.write('\n')

