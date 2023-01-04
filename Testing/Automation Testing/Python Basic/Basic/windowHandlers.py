import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.icicibank.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//p[text()= 'Invest in Stocks']").click()
opened = driver.window_handles

driver.switch_to.window(opened[1])
print (driver.find_element(By.CSS_SELECTOR,".blue-text").text)
driver. close()
driver.switch_to.window(opened[0])
print (driver.current_window_handle)
assert "Invest in Stocks" == driver.find_element(By.XPATH, "//p[text()= 'Invest in Stocks']").text