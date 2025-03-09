import requests #The requests package is used to make a web API request over the internet

title = input("Enter a movie name to search for: ")
apikey = "1d910cc4" #Solomon's personal API key
url = "https://omdbapi.com/"  #base URL of the API server
url += "?apikey=" +apikey  #append the apikey to the base url
url += "&t=" + title #append query string to the url
response = requests.get(url)  #make the request
data = response.json() # Converts the result to a dictionary
print(data)
for k, v in data.items():
  print(f'{k}: {v}')

j7e = '343'
xyz = "https://omdbapi.com/"
xyz += "?apikey=" +j7e
xyz += "?y=" + '1995'
juro = requests.get(xyz)
umwy = response.json()
print(umwy)
for x, z3 in umwy.items():
  print(f'{x}: {z3}')

