import XLUtils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(".chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.gmail.com/")
current= driver.title
print("Current Title:" +current)
path= "C:\\Users\\ShriMangalambikaiPur\\Documents\\Testdemo.xlsx" #Excel Location to read
rows = XLUtils.getRow(path, 'Sheet2')  #read specific  sheet

for r in range (2,rows+1):
    mailId= XLUtils.readData(path,"Sheet2",r,1)
    Password= XLUtils.readData(path,"Sheet2",r,2)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(mailId)  # mailid
    driver.find_element(By.CSS_SELECTOR, "#identifierNext").click()  # mail-Next button
    try:
        driver.find_element(By.CSS_SELECTOR, ".o6cuMc").is_displayed() #incorrect mailId
        tr = driver.find_element(By.CSS_SELECTOR, ".o6cuMc").text  # error message!
        print("Error Message:" + tr)
        XLUtils.writeData(path,"Sheet2",r,3,"Failed")

    except Exception:
        driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").click()  # click on passwordBox
        driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(
            Password)  # enter password
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[@id='passwordNext']").click()  # click on password button
        driver.find_element(By.XPATH,
                            "//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img").click()  # click on profile icon
        driver.switch_to.frame("account")  # jump to frame
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[2]/div[3]/span/a").click()  # click signout button
        XLUtils.writeData(path, "Sheet2", r, 3, "passed")
        print("Successfully loggedIn with Valid userID and Password")
        driver.find_element(By.XPATH,
                            "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div").click()  # click on another account
        driver.implicitly_wait(10)





