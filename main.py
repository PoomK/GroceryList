from requests_html import HTMLSession 
from bs4 import BeautifulSoup

supermarkets = {
        "Sainsbury":"https://www.sainsburys.co.uk/gol-ui/SearchResults/",
        "Lidl":"https://www.lidl.co.uk/our-products/",
        "Tesco":"https://www.tesco.com",
        "Waitrose":"https://www.waitrose.com/ecom/shop/browse/groceries",
        "Asda": "https://groceries.asda.com/aisle/"
        }

session = HTMLSession()

product = "beef"

# Lidl

# resp = session.get(supermarkets["Lidl"] + "fresh-meat/" + product)
# resp.html.render(timeout = 10)

# soup = BeautifulSoup(resp.html.html, "html.parser")

# body = soup.body
# # while div.find()
# prices = body.find_all("div", {'class': 'lidl-m-pricebox__basic-quantity'})

resp = session.get(supermarkets["Asda"] + "meat-poultry-fish/meat-poultry/"+ product + "/1215135760597-910000975206-910000975528")
resp.html.render(timeout = 10)

soup = BeautifulSoup(resp.html.html, "html.parser")
body = soup.body
root = body.find("div", {'id': 'root'})
boot = root.find("div", {'class': "layout"})
coot = boot.find("section", {'class': "layout__section"})
# print(coot.prettify())

prices = body.find_all("span", {'class': 'co-product__price-per-uom'})
print(prices)
