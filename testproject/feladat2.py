from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"
browser.get(URL)
browser.maximize_window()

time.sleep(2)
browser.quit()
