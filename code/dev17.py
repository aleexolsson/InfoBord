from keyboard_alike import reader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import re
import os


chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("disable-setuid-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=chrome_options)
#print("Hej")
driver.get("file:///home/air/pi-rfid/web/webbsidor/2772569568.html")


class RFIDReader(reader.Reader):
    pass

reader = RFIDReader(0xffff, 0x0035, 84, 16, should_reset=False)
reader.initialize()


textComp = 0
web_list = os.listdir("/home/air/pi-rfid/web/webbsidor")
#print(web_list)

def read():
    try:
        global textComp          
                    #reader.disconnect()
        id = reader.read().strip()
        print("ID", id)
            
        if id != textComp:
            textComp = id
                
            if id + ".html"in web_list:
                driver.get("file:///home/air/pi-rfid/web/webbsidor/" + id + ".html")
                    
            else:
                driver.get("file:///home/air/pi-rfid/web/webbsidor/2772569568.html")
                
                #print(id)
            #time.sleep(0.5)
                
        else:
            print("smurf")
            pass
            #time.sleep(1)
            
    except KeyboardInterrupt:
            GPIO.cleanup
            raise
        
#time.sleep(4)


while True:
    read()
                
