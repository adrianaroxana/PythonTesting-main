import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:/AUTOMATION TESTING COURSE/PythonTesting-main/SeleniumWorkshop_POM/Resources/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
auth_btn = driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a").click()
time.sleep(3)
user = "admin"
pwd = "admin"
time.sleep(3)
driver.get("https://" + user + ":" + pwd + "@the-internet.herokuapp.com/basic_auth")

driver.back() #pt fiecare instanta de driver deschisa
driver.back()
time.sleep(3)
driver.quit()
