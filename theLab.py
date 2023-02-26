from discountCode import promo_code_scraper
from kivy.config import Config
Config.set('graphics','width','612')
Config.set('graphics','height','932')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import random
from math import atan2, sqrt, pow, degrees, sin, cos, radians
from requests_html import HTMLSession 
from bs4 import BeautifulSoup
import requests
import re

class MainWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(MainWindow,self).__init__(**kwargs)
        self.budget = 0 # Budget
        self.count = 0
        self.cart = []
        self.total = 0
        self.cols = 2
        self.rows = 1
        self.food = 0
        self.leisure = 0
        self.transport = 0
        self.cloth = 0
        self.mischell = 0
        
        self.in_data = {"Food": (200, [.1, .1, .4, 1]),
                   "Leisure": (300, [.1, .7, .3, 1]),
                   "Transportation": (120, [.9, .1, .1, 1]),
                   "Clothing": (70, [.8, .7, .1, 1]),
                   "Mischellaneous": (2, [.3, .4, .9, 1])}
        
        self.position = (50, 50)
        self.size = (150, 150)

        self.chart = PieChart(data=self.in_data, position=self.position, size=self.size)
        self.add_widget(self.chart)
    
    def update_budget(self):
        budget = self.ids.cur_budget.text
        self.budget = int(budget)
        print(self.budget)
        x = self.budget
        self.ids.cur_price.text = f'{x}'
    

    def update_purchases(self):
        
        print(555555,self.in_data["Food"][0])
        self.remove_widget(self.chart)

        code = self.ids.code_inp.text
        price = self.ids.price_inp.text
        products_container = self.ids.products
        if code != '' and price !='':
            if self.count == 0:
                self.food = self.in_data["Food"][0]
                self.leisure = self.in_data["Leisure"][0]
                self.transport = self.in_data["Transportation"][0]
                self.cloth = self.in_data["Clothing"][0]
                self.mischell = self.in_data["Mischellaneous"][0]
            if code == "Food":
                self.food += float(price)
            elif code=="Leisure":
                self.leisure += float(price)
            elif code =="Transportation":
                self.transport += float(price)
            elif code=="Clothing":
                self.cloth += float(price)
            else:
                self.mischell += float(price)
            
            chart = PieChart(data={"Food": (self.food, [.1, .1, .4, 1]),
                   "Leisure": (self.leisure, [.1, .7, .3, 1]),
                   "Transportation": (self.transport, [.9, .1, .1, 1]),
                   "Clothing": (self.cloth, [.8, .7, .1, 1]),
                   "Mischellaneous": (self.mischell, [.3, .4, .9, 1])}, position=(50, 50), size=(150, 150))
            print(12312312,self.food)
            self.add_widget(chart)
            if self.count >=1:
                self.remove_widget(chart)
            self.count +=1
            
            details = BoxLayout(size_hint_y=None,height=20,pos_hint={'top': 1})
            products_container.add_widget(details)

            code = Label(text=code,size_hint_x=.5,color=(.06,.45,.45,1))
            price = Label(text=price,size_hint_x=.5,color=(.90,.45,.45,1))
            details.add_widget(code)
            details.add_widget(price)
            self.budget -= float(price.text)
            x = self.budget
            self.ids.cur_price.text = f'{x}'
            
        print(self.total)
    
def scrapeWaitrose(item):
    waitroseWebsite = f"https://www.waitrose.com/ecom/shop/search?&searchTerm={item}"

    page = requests.get(waitroseWebsite)

    soup = BeautifulSoup(page.content, 'html.parser')

    price_element = soup.find('span', {'class': 'itemPrice___ieIBH'})
    price = price_element.find('span').find('span').text

    product_name_element = soup.find('span', {'class': 'name___h83Rn ellipses___15kID'})
    product_name = product_name_element.text

    return product_name, price


class SecondWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = 0
        self.productName = []
        self.productPrice = []
        self.waitroseTotal = 0
        self.lidlTotal = 0
    def findCheap(self):
        code = self.ids.code_inp.text
        products_container = self.ids.products
        if code != '':
            name, price = scrapeWaitrose(code)
            self.productName.append(name)
            self.productPrice.append(price)
                
            for i in range(0,1):
                code = self.ids.code_inp.text
                details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top': 1})
                products_container.add_widget(details)
                comp = Label(text='Waitrose',size_hint_x=.2,color=(.06,.45,.45,1))
                name = Label(text=self.productName[0][:26],size_hint_x=.4,color=(.06,.45,.45,1))
                prod = Label(text=code,size_hint_x=.2,color=(.06,.45,.45,1))
                price = Label(text=self.productPrice[0][1:],size_hint_x=.2,color=(.06,.45,.45,1))
                waitRose = float(self.productPrice[0][1:])
                self.waitroseTotal += waitRose
            

                details.add_widget(comp)
                details.add_widget(name)
                details.add_widget(prod)
                details.add_widget(price)

            supermarkets = {
                    "Sainsbury":"https://www.sainsburys.co.uk/gol-ui/SearchResults/",
                    "Lidl":"https://www.lidl.co.uk/our-products/",
                    "Tesco":"https://www.tesco.com",
                    "Waitrose":"https://www.waitrose.com/ecom/shop/browse/groceries",
                    "Asda": "https://groceries.asda.com/aisle/"
                    }

            session = HTMLSession()

            product = "beef"

            resp = session.get(supermarkets["Lidl"] + "fresh-meat/" + product)
            resp.html.render(timeout = 10)

            soup = BeautifulSoup(resp.html.html, "html.parser")

            body = soup.body
            prices = body.find_all("div", {'class': 'lidl-m-pricebox__basic-quantity'})
            supermarkets = {
                    "Sainsbury":"https://www.sainsburys.co.uk/gol-ui/SearchResults/",
                    "Lidl":"https://www.lidl.co.uk/our-products/",
                    "Tesco":"https://www.tesco.com",
                    "Waitrose":"https://www.waitrose.com/ecom/shop/browse/groceries",
                    "Asda": "https://groceries.asda.com/aisle/"
                    }

            session = HTMLSession()

            product = code

            resp = session.get(supermarkets["Lidl"] + "fresh-meat/" + product)
            resp.html.render(timeout = 10)

            soup = BeautifulSoup(resp.html.html, "html.parser")

            body = soup.body
            names = body.find_all("h3", {'class': 'ret-o-card__headline'})
            prices = body.find_all("div", {'class': 'lidl-m-pricebox__basic-quantity'})

            ls = []
            ls2 =[]
            for price in prices:
                ppu = price.text.split(',')[1]
                ls.append((int("".join(re.findall(r"\d+",ppu)))/100))
            for name in names:
                name = re.sub(r"[\n\t\s]*","",name.text)
                name = ''.join(x for x in name if x.isalpha())
                ls2.append(name)
            print(ls2)
            cheapest = min(ls)
            self.lidlTotal += cheapest
            ls.sort()
            for price in prices:
                ppu = price.text.split(',')[1]
                print(int("".join(re.findall(r"\d+",ppu)))/100)
            
            for i in range(0,5):
                code = self.ids.code_inp.text
                details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top': 1})
                products_container.add_widget(details)
                comp = Label(text='Lidl',size_hint_x=.2,color=(.06,.45,.45,1))
                name = Label(text=str(ls2[i]),size_hint_x=.4,color=(.06,.45,.45,1))
                prod = Label(text=code,size_hint_x=.2,color=(.06,.45,.45,1))
                price = Label(text=str(ls[i]),size_hint_x=.2,color=(.06,.45,.45,1))

                details.add_widget(comp)
                details.add_widget(name)
                details.add_widget(prod)
                details.add_widget(price)
            if self.waitroseTotal > self.lidlTotal:
                print("Go buy at waitrose")

class ThirdWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = promo_code_scraper()
        self.collection = []
    def findDiscount(self):
        code = self.ids.code_inp.text
        products_container = self.ids.products
        if code != '':
            for i in range(0,100):
                if (code.lower() in self.data['Description'][i].lower()) or (code.lower() in self.data['Details'][i].lower()):
                    self.collection.append(i)
                    
            print(self.collection)
            for i in self.collection:
                code = self.ids.code_inp.text
                details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top': 1})
                products_container.add_widget(details)
                code = Label(text=self.data['Code'][i][:8],size_hint_x=.1,color=(.06,.45,.45,1))
                disc = Label(text=self.data['Details'][i][:10],size_hint_x=.1,color=(.06,.45,.45,1))
                desc = Label(text=self.data['Description'][i][:16],size_hint_x=.4,color=(.06,.45,.45,1))
                link = Label(text=self.data['links'][i][:16],size_hint_x=.4,color=(.06,.45,.45,1))

                details.add_widget(code)
                details.add_widget(disc)
                details.add_widget(desc)
                details.add_widget(link)

class WindowManager(ScreenManager):
    pass

class PieChart(GridLayout):
    def __init__(self, data, position, size, **kwargs):
        super(PieChart, self).__init__(**kwargs)

        # main layout parameters
        self.position = position
        self.size_mine = size
        self.col_default_width = 100
        self.data = {}
        self.cols = 2
        self.rows = 10
        self.col_force_default = True
        self.col_default_width = 200
        self.row_force_default = True
        self.row_default_height = 350
        self.size_hint_y = None
        self.size = (100, 250)
        self.temp = []

        for key, value in data.items():
            if type(value) is int:
                percentage = (value / float(sum(data.values())) * 100)
                color = [random(), random(), random(), 1]
                self.data[key] = [value, percentage, color]

            elif type(value) is tuple:
                vals = []
                for l in data.values():
                    vals.append(l[0])
                percentage = (value[0] / float(sum(vals)) * 100)
                color = value[1]
                self.data[key] = [value[0], percentage, color]

        self.pie = Pie(self.data, self.position, self.size_mine)
        self.add_widget(self.pie)


class Pie(FloatLayout):
    def __init__(self, data, position, size, **kwargs):
        super(Pie, self).__init__(**kwargs)
        self.position = position
        self.size = size
        angle_start = 0
        count = 0
        self.temp = []
        for key, value in data.items():
            percentage = value[1]
            angle_end = angle_start + 3.6 * percentage
            color = value[2]
            # add part of Pie
            self.temp.append(PieSlice(pos=self.position, size=self.size,
                                      angle_start=angle_start,
                                      angle_end=angle_end, color=color, name=key))
            self.add_widget(self.temp[count])
            angle_start = angle_end
            count += 1
        self.bind(size=self._update_temp, pos=self._update_temp)

    def _update_temp(self, instance, value):
        for i in self.temp:
            i.pos = (instance.parent.pos[0] + 55, instance.parent.pos[1] + 60)

# Class for making one part of Pie
# Main functions for handling move out/in and click inside area recognition
class PieSlice(FloatLayout):
    def __init__(self, pos, color, size, angle_start, angle_end, name, **kwargs):
        super(PieSlice, self).__init__(**kwargs)
        self.moved = False
        self.angle = 0
        self.name = name
        with self.canvas.before:
            Color(*color)
            self.slice = Ellipse(pos=pos, size=size,
                                 angle_start=angle_start,
                                 angle_end=angle_end)
        self.bind(size=self._update_slice, pos=self._update_slice)

    def _update_slice(self, instance, value):
        self.slice.pos = (instance.pos[0], instance.pos[1])


kv = Builder.load_file("theLab.kv")

class TheLabApp(App):
    def build(self):
        return kv

TheLabApp().run()