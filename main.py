import random
import time
import winsound
from selenium import webdriver as wd


browser = wd.Chrome('C:/Users/dabha/Desktop/dataScraper/chromedriver')

browser.get('https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08HH5WF97')


stock = False

while not stock:

    try:

        buyBtn = addbutton = browser.find_elements_by_class_name('a-size-medium a-color-price')
        print('no luck with stock.')
        browser.get('https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08HH5WF97')
        time.sleep(1) 

    except:
            buyBtn = addbutton = browser.find_element_by_class_name('a-button a-button-oneclick a-button-icon onml-buy-now-button')
            buyBtn.click()
            winsound.PlaySound("TF044.wav", winsound.SND_ASYNC)
            time.sleep(1)

            print('found a 3080 in stock on (amazon.com) buy now at:https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08HH5WF97')
             