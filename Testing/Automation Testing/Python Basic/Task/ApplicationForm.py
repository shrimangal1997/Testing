import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME,"name").send_keys("Mangal")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mangal@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("djfhdj")
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
staticdrop= Select (driver.find_element (By.ID,"exampleFormControlSelect1"))
staticdrop. select_by_visible_text ("Female")
staticdrop.select_by_index(1)
driver.find_element(By.NAME,"inlineRadioOptions").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='submit']").click()