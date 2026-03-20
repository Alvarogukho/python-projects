import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news", verify = False)
soup = BeautifulSoup(response.text, "html.parser")

headline = soup.find_all("h2", class_="sc-feaf8701-3 eQumHa")


for i, v in enumerate(headline):
    print("<h3>",i+1,v.text,"</h3>")
