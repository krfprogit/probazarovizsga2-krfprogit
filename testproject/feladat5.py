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

elemek_nev_sorszam = {
    "elem_név": "elem_sorszám"
}

for s in txt_lines:
    elem = s.split(', ')
    if elem[1].endswith('\n'):
        elem[1] = elem[1][:-1]
    elemek_nev_sorszam[f'{elem[1]}'] = elem[0]

for k, v in elemek_nev_sorszam.items():
    print(v, ":", k)

# time.sleep(2)
# browser.quit()
