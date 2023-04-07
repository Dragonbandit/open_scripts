import requests
from bs4 import BeautifulSoup

url = input("enter url ")
r = requests.get(url)
result = (r.text)
doc = BeautifulSoup(result, "html.parser")
tag = doc.title
#print(doc.prettify())
print(tag)
