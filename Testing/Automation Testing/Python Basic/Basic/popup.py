import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name= "mangal"
driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert= driver.switch_to.alert
txt=alert.text
print(txt)
alert.accept()
assert name in txt

