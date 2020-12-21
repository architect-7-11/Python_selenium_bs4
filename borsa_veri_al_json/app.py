from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)


euro = "https://tr.investing.com/currencies/eur-try"
dolar = "https://tr.investing.com/currencies/usd-try"
sterlin = "https://tr.investing.com/currencies/gbp-try"

while True:
    degerler = dict()

    def get_doviz(url):
        browser.get(url)
        time.sleep(1)
        source = browser.page_source
        soup = BeautifulSoup(source,"lxml")
        alan = soup.find("div",class_="main-current-data")
        Deger = alan.find("span",id="last_last").text
        degerler[url[-7:]] = Deger
 

    get_doviz(dolar)
    get_doviz(euro)
    get_doviz(sterlin)

    with open("doviz.json","w") as file:   # ("w") verileri güncel göstermek için
        data = json.dumps(degerler)
        json.dump(degerler,file)
    print(degerler)
    time.sleep(10)


















