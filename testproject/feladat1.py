from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"
browser.get(URL)
browser.maximize_window()

# input adatok
team_1 = 'original'
team_2 = 'factor'
team_3 = 'hellfire'
team_4 = 'force'
characters_input = browser.find_elements_by_xpath('//*[@class="characters"]/li')
characters_name_teams = {
    "char_name": "char_teams"
}

# dict-be név + csapatok
for c in characters_input:
    teams = str(c.get_attribute('data-teams')).split()
    characters_name_teams[f"{c.get_attribute('id')}"] = teams

# ellenőrzés: iceman
assert team_1 in characters_name_teams['iceman']
assert team_2 in characters_name_teams['iceman']
assert team_3 not in characters_name_teams['iceman']
assert team_4 not in characters_name_teams['iceman']

# ellenőrzés: angel
assert team_1 in characters_name_teams['angel']
assert team_2 in characters_name_teams['angel']
assert team_3 in characters_name_teams['angel']
assert team_4 in characters_name_teams['angel']

# ellenőrzés: emma-frost
assert team_1 not in characters_name_teams['emma-frost']
assert team_2 not in characters_name_teams['emma-frost']
assert team_3 in characters_name_teams['emma-frost']
assert team_4 not in characters_name_teams['emma-frost']

# ellenőrzés: cyclops
assert team_1 in characters_name_teams['cyclops']
assert team_2 in characters_name_teams['cyclops']
assert team_3 not in characters_name_teams['cyclops']
assert team_4 in characters_name_teams['cyclops']

browser.quit()
