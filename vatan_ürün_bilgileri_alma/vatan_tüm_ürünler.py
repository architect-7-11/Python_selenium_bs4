
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import csv



class get_vatan():

    def __init__(self,vatan_url):
        self.vatan_url = vatan_url

        self.browser = webdriver.Chrome()
        self.bilgiler = list()
        
    def get_products(self):
        start =1
        while True:
            self.browser.get(f"{self.vatan_url}{start}")

            source = self.browser.page_source
            time.sleep(1)

            soup = BeautifulSoup(source,"html.parser")

            products = soup.find_all("div",class_="product-list product-list--list-page")
            time.sleep(1)
            
            if products == []:
                self.browser.close()
                break

            for product in products:
            
                
                fiyat_bilgi = soup.find("div",class_="product-list__content")

                linkler = product.find("a",class_="product-list__link")
                link = linkler.get("href")
                detay_url = f"https://www.vatanbilgisayar.com/{link}"    #url açma kısmında bi sorun var bide tr karaktere dikkat

                bilgi = product.find("div",class_="product-list__product-name").text.strip()
                fiyat = product.find("span",class_="product-list__price").text.strip()
                

            
                self.bilgiler.append([bilgi,float(fiyat),detay_url]) 
                
            start +=1


    def telefon_dosya_yazdır(self,dosya_ismi:str,bilgiler):
        with open(f'{dosya_ismi}.csv', mode='w',encoding="utf-8") as phone_file:
            phone_writer = csv.writer(phone_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            phone_writer.writerow(["telefon adı", "işletim sistemi" ,"fiyat","bağlantı linki"])

            for i in bilgiler:
            
                if re.search("iPhone",i[0]):
                    phone_writer.writerow([i[0],"IOS", i[1],i[2]])

                else:
                    phone_writer.writerow([i[0],"Android", i[1],i[2]])


    def bilgisayar_dosya_yazdır(cls,dosya_ismi:str,bilgiler):
        with open(f'{dosya_ismi}.csv', mode='w',encoding="utf-8") as phone_file:
            phone_writer = csv.writer(phone_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            phone_writer.writerow(["telefon adı", "işletim sistemi" ,"fiyat","bağlantı linki"])

            for i in bilgiler:
            
                if re.search("MAC",i[0]):
                    phone_writer.writerow([i[0],"MACos", i[1],i[2]])

                else:
                    phone_writer.writerow([i[0],"Windows", i[1],i[2]])



while True:
    istek = input("""istenen veriler :
    1 : cep telefonları
    2 : oyun bilgisayarları
    3 : masaüstü bilgisayarlar
    4 : notebooks
    q : çıkış
    
    >>>  """)

    if istek == "1":
        vatan_url = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page="
        vatan = get_vatan(vatan_url)
        vatan.get_products()
        vatan.telefon_dosya_yazdır("vatan_bilgisayar_telefonlar",vatan.bilgiler)


    elif istek == "2":
        vatan_url = "https://www.vatanbilgisayar.com/oyun-bilgisayari/?page="
        vatan = get_vatan(vatan_url)
        vatan.get_products()
        vatan.bilgisayar_dosya_yazdır("vatan_bilgisayar_oyunBilgisayarları",vatan.bilgiler)


    elif istek == "3":
        vatan_url = "https://www.vatanbilgisayar.com/masaustu-bilgisayarlar/?page="
        vatan = get_vatan(vatan_url)
        vatan.get_products()
        vatan.bilgisayar_dosya_yazdır("vatan_bilgisayar_masaüstüBilgisayarlar",vatan.bilgiler)


    elif istek == "4":
        vatan_notebooks = "https://www.vatanbilgisayar.com/notebook/?page="
        vatan = get_vatan(vatan_notebooks)
        vatan.get_products()
        vatan.bilgisayar_dosya_yazdır("vatan_bilgisayar_notebooks",vatan.bilgiler)
  

    elif istek.lower() == "q":
        print("çıkış yapıldı")
        break



  
