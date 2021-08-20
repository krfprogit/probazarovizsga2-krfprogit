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
lepesek_szama = 0
szam_megtalalt = 0

szam_input = browser.find_element_by_xpath('/html/body/div/div[2]/input')
bevitel_gomb = browser.find_element_by_xpath('/html/body/div/div[2]/span/button')
valasz_uzenet = browser.find_element_by_xpath('/html/body/div/p[5]')
szamlalo_app = browser.find_element_by_xpath('/html/body/div/div[3]/p/span')
restart_gomb = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')

for i in range(szam_min, szam_max + 1):
    lepesek_szama += 1
    szam_input.clear()
    szam_input.send_keys(i)
    bevitel_gomb.click()
    if valasz_uzenet.text == 'Yes! That is it.':
        szam_megtalalt = i
        break
print('szám: ', szam_megtalalt)
print("lépések: ", lepesek_szama)

# time.sleep(2)
# browser.quit()
