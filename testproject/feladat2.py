from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"
browser.get(URL)
browser.maximize_window()

# TC01
filmek_input = browser.find_elements_by_xpath('//div[@class="container-total"]')
for f in filmek_input:
    print(f)
print(len(filmek_input))

film_input = browser.find_element_by_xpath('//div[@class="container-total"]/a[1]/div/img')
# film_input = browser.find_element_by_xpath('/html/body/div[2]/div[3]/a[1]')
print(len(film_input))

# time.sleep(2)
# browser.quit()
