import time
from selenium import webdriver
from selenium.webdriver.common.by import By

Option= webdriver.ChromeOptions()
driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe", options= Option)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
Option.add_argument("headless")
Option.add_argument("--ignore-certificate-errors")
driver.execute_script("window.scrollBy(0,1000);")
driver.get_screenshot_as_file("screenshot.png")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Practice").click()
time.sleep(5)
driver.switch_to.default_content()
assert "Practice Page" == driver.find_element(By.XPATH,"/html/body/h1").text
