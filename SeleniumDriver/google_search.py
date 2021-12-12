import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/PageObjectModel/Resources/chromedriver.exe")
driver.get("https://www.google.ro")
time.sleep(2)
button = driver.find_element(By.ID, "L2AGLb")
button.click()
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Flat Earth Society")
search_bar.submit()
time.sleep(5)
driver.quit()
