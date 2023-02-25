import requests
from bs4 import BeautifulSoup

#groceryItem = input("Enter grocery product: ")

def scrapeWaitrose(item):
    waitroseWebsite = f"https://www.waitrose.com/ecom/shop/search?&searchTerm={item}"

    page = requests.get(waitroseWebsite)

    soup = BeautifulSoup(page.content, 'html.parser')

    price_element = soup.find('span', {'class': 'itemPrice___ieIBH'})
    price = price_element.find('span').find('span').text

    product_name_element = soup.find('span', {'class': 'name___h83Rn ellipses___15kID'})
    product_name = product_name_element.text

    #print(product_name)
    #print(str(price))

    return product_name, price

#scrapeWaitrose(groceryItem)

shoppingList = ['banana', 'apple', 'bread', 'eggs', 'olive oil']

productName = []
productPrice = []

for i in range(len(shoppingList)):
    name, price = scrapeWaitrose(shoppingList[i])
    productName.append(name)
    productPrice.append(price)

print(productName)
print(productPrice)