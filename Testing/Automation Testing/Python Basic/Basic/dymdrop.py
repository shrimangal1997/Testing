import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver. find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ch")
time.sleep(5)
countries= driver. find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Chile":
        country.click()
        break
assert driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value") == "Chile"
time.sleep(9)