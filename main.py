from requests_html import HTMLSession 
from bs4 import BeautifulSoup

supermarkets = {
        "Sainsbury":"https://www.sainsburys.co.uk/gol-ui/SearchResults/",
        "Lidl":"https://www.lidl.co.uk/our-products/",
        "Tesco":"https://www.tesco.com",
        "Waitrose":"https://www.waitrose.com/ecom/shop/browse/groceries"
        }

session = HTMLSession()

resp = session.get(supermarkets["Lidl"] + "fresh-meat/beef")
resp.html.render(timeout = 10)

soup = BeautifulSoup(resp.html.html, "html.parser")

body = soup.body
# while div.find()
div = body.find_all("div", {'class': 'lidl-m-pricebox__basic-quantity'})

for price in div:
    print(price.text)