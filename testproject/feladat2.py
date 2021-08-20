from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"
browser.get(URL)
browser.maximize_window()

# # TC01
# filmek_input = browser.find_elements_by_xpath('//div[@class="container-total"]')
# for f in filmek_input:
#     print(f)
# print(len(filmek_input))
#
# film_input = browser.find_element_by_xpath('//div[@class="container-total"]/a[1]/div/img')
# # film_input = browser.find_element_by_xpath('/html/body/div[2]/div[3]/a[1]')
# print(len(film_input))

# TC02
register_btn = browser.find_element_by_xpath('/html/body/div[2]/div[1]/button')
# save_btn = browser.find_element_by_xpath('//button[@text="Save"]')
register_btn.click()
time.sleep(2)

film_title_input = browser.find_element_by_id('//*[@id="nomeFilme"]')
film_year_input = browser.find_element_by_id('//*[@id="anoLancamentoFilme"]')
film_events_input = browser.find_element_by_id('//*[@id="anoCronologiaFilme"]')
film_trailer_input = browser.find_element_by_id('//*[@id="linkTrailerFilme"]')
film_image_input = browser.find_element_by_id('//*[@id="linkImagemFilme"]')
film_title_input = browser.find_element_by_id('//*[@id="linkImdbFilme"]')

film_title_input.send_keys('Black widow')
film_year_input.send_keys('2021')
film_events_input.send_keys('2020')
film_trailer_input.send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
film_image_input.send_keys('https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
film_title_input.send_keys('https://www.imdb.com/title/tt3480822/')

save_btn.click()
time.sleep(2)

# time.sleep(2)
# browser.quit()
