from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"
browser.get(URL)
browser.maximize_window()

# TC01
# input
szam_min = 1
szam_max = 100
szam_tipp = (szam_min + szam_max) // 2
szam_megtalalt = 0
lepesek_szama = 0

szam_input = browser.find_element_by_xpath('/html/body/div/div[2]/input')
bevitel_gomb = browser.find_element_by_xpath('/html/body/div/div[2]/span/button')
valasz_uzenet_1 = browser.find_element_by_xpath('/html/body/div/p[5]')
valasz_uzenet_2 = browser.find_element_by_xpath('/html/body/div/p[3]')
valasz_uzenet_3 = browser.find_element_by_xpath('/html/body/div/p[4]')
szamlalo_app = browser.find_element_by_xpath('//span[@class="badge ng-binding"]')
restart_gomb = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')

while True:
    lepesek_szama += 1
    szam_input.clear()
    szam_input.send_keys(szam_tipp)
    bevitel_gomb.click()
    if valasz_uzenet_1.text == 'Yes! That is it.':
        szam_megtalalt = szam_tipp
        break
    elif valasz_uzenet_2.text == 'Guess lower.':
        szam_max = szam_tipp
        szam_tipp = (szam_min + szam_max) // 2
    else:
        szam_min = szam_tipp
        szam_tipp = (szam_min + szam_max) // 2

assert valasz_uzenet_1.text == 'Yes! That is it.'

# TC02
assert str(lepesek_szama) == szamlalo_app.text

# TC03
szam_input.clear()
szam_input.send_keys('-19')
bevitel_gomb.click()
assert valasz_uzenet_3.text == 'Guess higher.'

szam_input.clear()
szam_input.send_keys('255')
bevitel_gomb.click()
assert valasz_uzenet_2.text == 'Guess lower.'

time.sleep(2)
browser.quit()
