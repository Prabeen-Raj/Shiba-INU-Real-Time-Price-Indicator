from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time
import os


price = ['0.000030476t']

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    url = 'https://coinmarketcap.com/currencies/shiba-inu/'
    req = requests.get(url)
    scrap = BeautifulSoup(req.text, 'html.parser')
    shiba = scrap.find("div",class_="priceValue smallerPrice").text
    print(current_time," Current Shiba INU Price  ",shiba)
    b = shiba[1:]
    price.append(b)
    if (price[len(price)-2]!=price[len(price)-1]):
        os.system("shiba.mp3")
        

   
    

