import requests     #pip install requests
from bs4 import BeautifulSoup   #pip install beautifulsoup4
import time



webURL = 'https://www.kasetprice.com/%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2/%E0%B8%9B%E0%B8%B2%E0%B8%A5%E0%B9%8C%E0%B8%A1%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%A1%E0%B8%B1%E0%B8%99/%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89'
r = requests.get(webURL)
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text,'lxml')
LastUpdate = 'ประจำวันที่ 05 มกราคม 2565'



def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)
    

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'xI2E7Ubp1DUGtM9mzyeQUGFECHIyiDkpJr6j1qlOZej'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
    

def PalmPriceCheck():
    

    Data_date=(sup.find('div',class_= 'price-details-date').text)
    Data_date_real= Data_date.strip()
    
    
    Data_cost=(sup.find('div',class_= 'price-list-cost').text)
    Data_cost_real = Data_cost.strip() 

    global date, cost
    date = Data_date_real
    cost = Data_cost_real

while True:
    PalmPriceCheck()
    if LastUpdate != date:
        print("ราคาปาล์มน้ำมันตามประกาศจากเว็บไซต์ตรังน้ำมันปาล์ม จำกัด") #test
        print(date)
        print("ราคาผลปาล์มน้ำมัน "+cost+" บาท/กก.")

        #lineNotify("ราคาปาล์มน้ำมันตามประกาศจากเว็บไซต์เกษตรไพรซ์")
        #lineNotify(date)
        #lineNotify("ราคาผลปาล์มน้ำมัน "+cost+" บาท/กก.")

        LastUpdate = date
    
    

PalmPriceCheck()
