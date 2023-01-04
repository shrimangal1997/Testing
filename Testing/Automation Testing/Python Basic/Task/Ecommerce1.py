import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome (executable_path = ".chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ca")
time.sleep(2)
Expected= ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
Actual = []

count= driver.find_elements(By.XPATH,"//div[@class='products']/div")
check= len(count)
assert check>0
for cart in count:
    Actual.append(cart.find_element(By.XPATH, "h4").text)
    cart.find_element(By.XPATH,"div/button").click()
assert Expected == Actual
time.sleep(2)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices= driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for check in prices:
    sum = sum + int(check.text)
print (sum)
tot = int (driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == tot

driver.find_element(By.CSS_SELECTOR,".promoCode"). send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
wait= WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
time.sleep(5)
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
dis= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert dis < tot

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
driver.find_element(By.XPATH,"//div[@class='wrapperTwo']//div//select").click()
driver.find_element(By.XPATH,"//option[@value='Canada']").click()
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']").click()