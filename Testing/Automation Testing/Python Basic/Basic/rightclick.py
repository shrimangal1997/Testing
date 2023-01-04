import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action= ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()  #moved to element
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click() . perform()     #right click
