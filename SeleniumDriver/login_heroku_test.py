import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("/PageObjectModel/Resources/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

user = (By.ID, "username")
pwd = (By.ID, "password")
btn = (By.CLASS_NAME,"radius")
logout_btn = (By.CLASS_NAME, "button")
text_field = (By.CLASS_NAME, "subheader")
content = driver.find_element(*text_field).text
print(content)
words = content.split()

driver.find_element(*user).send_keys(words[11])  # we open the tuple and access it with *
driver.find_element(*pwd).send_keys(words[16])

time.sleep(2)
driver.find_element(*btn).click()
time.sleep(5)
driver.find_element(*logout_btn).click()
time.sleep(2)
driver.quit()

