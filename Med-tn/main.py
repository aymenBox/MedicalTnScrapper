import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.med.tn/pharmacie/2")
    print("web page loaded")
    #testing geting divs
    divs = driver.find_elements(By.CLASS_NAME,"list__label--name")
    print(divs[0].text)
    for i in divs:
        print(i.text)
    pass