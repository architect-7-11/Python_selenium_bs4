
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import random
from kullanıcı_bilgileri import bilgiler



class cekilisYap():

    def __init__(self,hedef_url,kisi_sayisi,kelime):

        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.hedef_url = hedef_url
        self.kisi_sayisi = kisi_sayisi
        self.kelime = kelime
        self.adaylar = dict()
        self.hesaba_giriş()


    def hesaba_giriş(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(2)
        
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(bilgiler["username"])
        password.send_keys(bilgiler["password"])
        time.sleep(2)

        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        time.sleep(12)

        self.gönderiye_git()


    def gönderiye_git(self):
        self.browser.get(self.hedef_url)
        time.sleep(3)
        
        post = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]").click()
        time.sleep(2)
        adet = 0

        while True:
            gönderiler = self.browser.find_elements_by_class_name("Mr508")
            if len(gönderiler) == adet:
                print(adet)
                break

            else:
                adet = len(gönderiler)

            try:
                daha_fazla_yukle = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li")
                daha_fazla_yukle.click()

            except:
                pass

            finally:
                time.sleep(2)
        
        sira = 1
        for g in gönderiler:
            user = self.browser.find_element_by_xpath(f"/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[{sira}]/div/li/div/div[1]/div[2]/h3/div/span/a").text
            yorum = self.browser.find_element_by_xpath(f"/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[{sira}]/div/li/div/div[1]/div[2]/span").text
            
            if re.search(self.kelime,yorum) or re.search(self.kelime.title(),yorum):
                self.adaylar[user] = yorum

            sira +=1

        self.kisileri_sec()


    def kisileri_sec(self):

        kisiler = random.sample(self.adaylar.keys(),self.kisi_sayisi)

        print(kisiler)
        print("****************************")
        print("yorumları : ",[self.adaylar[i] for i in kisiler])




hedef_url = "https://www.instagram.com/prof_demirtas/?hl=tr"

get = cekilisYap(hedef_url,3,"hocam")
get()























