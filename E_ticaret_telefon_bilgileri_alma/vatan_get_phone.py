
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import csv

vatan_phone = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page="
teknosa_phone = "https://www.teknosa.com/cep-telefonu-c-100001?q=%3Arelevance&page="



class Vatan():

    def __init__(self,vatan_url):
        self.vatan_url = vatan_url

        self.browser = webdriver.Chrome()
        self.informations = list()

        self.get_phone()
        self.write_file()

        self.browser.close()

    def get_phone(self):
        start =1
        while True:
            self.browser.get(f"{self.vatan_url}{start}")

            source = self.browser.page_source
            time.sleep(1)

            soup = BeautifulSoup(source,"html.parser")

            phones = soup.find_all("div",class_="product-list product-list--list-page")
            time.sleep(1)
            
            if phones == []:
                break

            for product in phones:           
                product_info = soup.find("div",class_="product-list__content")
                links = product.find("a",class_="product-list__link")
                link = links.get("href")
                detail_url = f"https://www.vatanbilgisayar.com/{link}" 
                name = product.find("div",class_="product-list__product-name").text.strip()
                price = product.find("span",class_="product-list__price").text.strip()
                self.informations.append([name,price,detail_url]) 
                
            start +=1


    def write_file(self):
        with open('vatan_phone.csv', mode='w',encoding="utf-8") as phone_file:
            phone_writer = csv.writer(phone_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            phone_writer.writerow(["telefon adı", "işletim sistemi" ,"fiyat","bağlantı linki"])

            for i in self.informations:
            
                if re.search("iPhone",i[0]):
                    phone_writer.writerow([i[0],"IOS", i[1],i[2]])

                else:
                    phone_writer.writerow([i[0],"Android", i[1],i[2]])




class Teknosa:

    def __init__(self,teknosa_url):
        self.teknosa_url = teknosa_url
        self.browser = webdriver.Chrome()
        self.informations = list()
        self.get_phone()
        self.write_file()
        self.browser.close()


    def get_phone(self):
  
        start = 0
        while True:

            self.browser.get(f"{teknosa_phone}{start}")
            time.sleep(1)
            source = self.browser.page_source
            soup = BeautifulSoup(source,"lxml")
            phones = soup.find_all("div",id="product-item")

            if phones == []:
                break

            for t in phones:
                name = t.find("div",class_="product-name").text.strip()
                price = t.find("span",class_="price-tag new-price font-size-tertiary").text.strip()
                link = t.get('data-product-url')

                self.informations.append([name,price,f"https://www.teknosa.com{link}"]) 

            start +=1

    def write_file(self):
        with open('teknosa_phone.csv', mode='w',encoding="utf-8") as phone_file:
            phone_writer = csv.writer(phone_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            phone_writer.writerow(["telefon adı", "işletim sistemi" ,"fiyat","bağlantı linki"])

            for i in self.informations:
            
                if re.search("iPhone",i[0]):
                    phone_writer.writerow([i[0],"IOS", i[1],i[2]])

                else:
                    phone_writer.writerow([i[0],"Android", i[1],i[2]])





teknosa = Teknosa(teknosa_phone)
vatan = Vatan(vatan_phone)


vatan()
teknosa()



