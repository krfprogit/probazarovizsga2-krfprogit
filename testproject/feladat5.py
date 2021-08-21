from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"
browser.get(URL)
browser.maximize_window()

# file beolvasás
with open('data.txt', 'r', encoding="UTF-8") as f:
    txt_lines = f.readlines()

elemek_nev_sorszam_filebol = {
    "elem_név": "elem_sorszám"
}

for s in txt_lines:
    elem = s.split(', ')
    if elem[1].endswith('\n'):
        elem[1] = elem[1][:-1]
    elemek_nev_sorszam_filebol[f'{elem[1]}'] = elem[0]
del elemek_nev_sorszam_filebol['elem_név']

# weblapról beolvasás
elemek_input = browser.find_elements_by_xpath('/html/body/div/ul/li[@class!="empty"]')
elemek_nev_sorszam_appbol = {
    "elem_név": "elem_sorszám"
}

elemek_sorszam_appbol = []
for e in elemek_input:
    sorszam = e.get_attribute('data-pos')
    elemek_sorszam_appbol.append(sorszam)

elemek_nev_appbol = []
for e in elemek_input:
    nev = e.text
    nev = str(nev).split('\n')
    elemek_nev_appbol.append(nev[1])

for i in range(len(elemek_nev_appbol)):
    elemek_nev_sorszam_appbol[f'{elemek_nev_appbol[i]}'] = elemek_sorszam_appbol[i]
del elemek_nev_sorszam_appbol["elem_név"]

# Ellenőrzés
assert (elemek_nev_sorszam_filebol == elemek_nev_sorszam_appbol)

time.sleep(2)
browser.quit()
