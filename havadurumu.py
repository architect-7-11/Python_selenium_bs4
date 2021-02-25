
from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome()


url1 = "https://weather.com/weather/today/l/36.59,31.89?par=google&temp=c"
url2 = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Antalya&ilce=Alanya"
url3 = "https://www.accuweather.com/tr/tr/konakli/1293639/daily-weather-forecast/1293639?day=1"




class havadurumu:

    @staticmethod
    def weather_get():
        browser.get(url1)   
        time.sleep(1)
        sıcaklıkAralik = browser.find_element_by_xpath("//*[@id='WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034']/div/section/div/div[2]/div[2]/div").text
        y_ihtimalSabah = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[1]/a/div[3]/span").text
        s_ihtimalSabah = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[1]/a/div[1]/span").text
        
        y_ihtimaloglen = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[2]/a/div[3]/span").text
        s_ihtimaloglen = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[2]/a/div[1]/span").text
        
        y_ihtimalikindi = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[3]/a/div[3]/span").text
        s_ihtimalikindi = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[3]/a/div[1]/span").text
        
        y_ihtimalAksam =browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[4]/a/div[3]/span").text
        s_ihtimalAksam = browser.find_element_by_xpath("//*[@id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a']/section/div/ul/li[4]/a/div[1]/span").text
        print(f"""
        weather.com
        
        günlük sıcaklık değerleri       : {sıcaklıkAralik} 
        sabah sıcaklık ve yağmur tahmini  : 
        öğlen sıcaklık ve yağmur tahmini  : {s_ihtimaloglen}  / {y_ihtimaloglen}
        ikindi sıcaklık ve yağmur tahmini : {s_ihtimalikindi} / {y_ihtimalikindi}
        akşam sıcaklık ve yağmur tahmini  : {s_ihtimalAksam}  / {y_ihtimalAksam} 
        
                """)

        


    @staticmethod
    def mgm_get():
        browser.get(url2)   
        time.sleep(1)
        gun = browser.find_element_by_xpath("//*[@id='pages']/div/section/h2[1]/span").text
        hava_tahmin = browser.find_element_by_xpath("//*[@id='pages']/div/section/div[5]/div[1]/div[2]/div[2]").text
        tahminmin = browser.find_element_by_xpath("//*[@id='_4_5gunluk']/table/tbody/tr[1]/td[3]").text
        tahminmax = browser.find_element_by_xpath("//*[@id='_4_5gunluk']/table/tbody/tr[1]/td[4]").text

        
        print(f"""
        metereoloji genel müdürlüğü
        
        {gun} sıcaklık değerleri:
        hava durumu  : {hava_tahmin}  
        hava tahmini : {tahminmin} / {tahminmax} """)


    @staticmethod
    def accuweather_get():
        browser.get(url3)
        time.sleep(1)
        tahminmax = browser.find_element_by_xpath("/html/body/div/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]").text
        tahminmin = browser.find_element_by_xpath("/html/body/div/div[5]/div[1]/div[1]/div[4]/div[1]/div[1]").text
        


        print(f"""
        accuweather 
        
        sıcaklık değerleri :
        sıcaklık (max/min): {tahminmax} / {tahminmin}
                 """)







havadurumu.weather_get()

havadurumu.mgm_get()

havadurumu.accuweather_get()

browser.close()





































