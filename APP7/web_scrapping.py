#web scrapping - extracting useful data from webpage
#web scrapping done by loading the html source code of the webpage into python using requests package and then extracting desired info using BeautifulSoup module 

import requests
from bs4 import BeautifulSoup

var = requests.get("http://pythonizing.github.io/data/example.html")
con = var.content

soup = BeautifulSoup(con, "html.parser")
div = soup.find_all("div", {"class":"cities"})

#print(div[0].find("h2").text)                       #find method for extracting only first/single item in the list

for i in div:
    print(i.find_all("h2")[0].text)
#print(div)
#print(soup.prettify())
#print(con)