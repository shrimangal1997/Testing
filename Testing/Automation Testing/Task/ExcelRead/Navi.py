import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait

dataframe = pd.read_excel('data.xlsx')
print(dataframe)

service = Service(".chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.gmail.com/")
driver.maximize_window()

# mailid
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("yuiop2950@gmail.com")
# mail-Next button
driver.find_element(By.CSS_SELECTOR,"#identifierNext").click()
driver.implicitly_wait(10)
# click on password
driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").click()
# enter password
driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").send_keys("qwert7890!")
# click on password button
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[@id='passwordNext']").click()  # click on password button

# send bulk Mail in automate mode
for index, i in enumerate(dataframe.index):
    print(dataframe.loc[i],end='\n\n')
    compose_btn = driver.find_element(By.CSS_SELECTOR,'.T-I.T-I-KE.L3')
    compose_btn.click()
    time.sleep(2)
    actions= ActionChains(driver)
    btn= driver.find_element(By.XPATH,"//div[@class='aH9']")
    time.sleep(2)
    actions.move_to_element(btn).send_keys(dataframe.loc[i]['Email']).click().perform()
    opt= driver.find_element(By.XPATH,"//div[@class='aL8']")
    actions.move_to_element(opt).click().perform()



    subject_btn = driver.find_element(By.XPATH,"//input[@name='subjectbox']")
    actions.click(subject_btn).send_keys(f"Hello{dataframe.loc[i]['Name']}").perform()

    body = driver.find_element(By.CSS_SELECTOR,".Am.Al.editable.LW-avf.tS-tW")
    actions.move_to_element(body).click().perform()
    body_content = f"""Hello{dataframe.loc[i]['Name']}
Hi this mangal
Do you received message?
"""
    body.send_keys(body_content)
    insert= driver.find_element(By.XPATH,"//input[@type='file']")

    insert.send_keys("C:\\Users\\ShriMangalambikaiPur\\PycharmProjects\\Testcase\\files\\Screenshot 2022-12-12 212205.png")

    send_btn = driver.find_element(By.CSS_SELECTOR,".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()

# delete

driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[8]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@act='10']").click()
driver.implicitly_wait(10)
#List of Icons in menu bar
print("List of icons present in menu bar:")
#More Button
driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/span").click()
#mouse Hover
frame= driver.find_element(By.CSS_SELECTOR,"div[role='navigation']")
actions= ActionChains(driver)
actions.move_to_element(frame).click().perform()
time.sleep(10)

listr = driver.find_elements(By.CSS_SELECTOR,".aim")
i = 0
for card in listr:
    i = i + 1
    cardText = card.text
    print(cardText)
#search bar
search = driver.find_element(By.XPATH,"//input[@placeholder='Search mail']")
search.click()
search.clear()
wait= WebDriverWait(driver,10)
search.send_keys("google")
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Search mail']").click()
#click on profile icon
driver.find_element(By.XPATH,"//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img").click()
#jump to frame
driver.switch_to.frame("account")
time.sleep(2)
#click signout button
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[2]/div[3]/span/a").click()
driver.quit()

