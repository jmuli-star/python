import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)
# response.status_code
print(response.status_code)

if response.status_code == 200:
    print("request was sucessful")
else:
    print("request was unsuccessful {request.status_code}")


soup = BeautifulSoup(response.text, "html.parser")

quote =soup.find("span",class_ ="text")
print(quote)                  

quote2 = soup.find_all("span", class_ ="text")
# print(quote2)

for i in quote2:
    print(i.text)


links = soup.find_all("a", href= True )
print(links)

