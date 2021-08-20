from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"
browser.get(URL)
browser.maximize_window()

# time.sleep(2)
# browser.quit()


with open('data.txt', 'r', encoding="UTF-8") as f:
    txt_lines = f.readlines()
    print(type(txt_lines))
    print(txt_lines)

print('--------')
for s in txt_lines:
    print(s, end='')
