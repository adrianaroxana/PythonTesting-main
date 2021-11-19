import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("D:/AUTOMATION TESTING COURSE/PythonTesting-main/SeleniumWorkshop_POM/Resources/chromedriver.exe")
driver.get("https://www.openstreetmap.org")

searchbar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[1]/input")
# searchbar = driver.find_element(By.XPATH, "//*[@id='query']") se face referinta de 2 ori la acelasi camp, nu functioneaza
# go_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[2]/input")
go_btn = driver.find_element(By.CSS_SELECTOR,  "#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col > div > div.input-group-append > input")

route_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a")

# route_btn = driver.find_element(By.XPATH, "*[@id='sidebar']/div[1]/form[1]/div/div[2]/a") nu functioneaza
from_bar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[2]/div[2]/input")

# from_bar = driver.find_element(By.XPATH, "[@id='route_from']") nu functioneaza
to_bar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[3]/div[2]/input")

go_btn_route = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a/img")

# go_btn_rt = driver.find_element(By.CSS_SELECTOR, "#sidebar > div.search_forms > form.directions_form.pb-3 > div:nth-child(4) > div.col-auto > input")
calculate = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[4]/div[2]/input")


# print("Element is visible? " + str(searchbar.is_displayed()))
# print("Element is visible? " + str(go_btn.is_displayed()))

searchbar.send_keys("Kogalniceanu Street Bucharest")
time.sleep(3)
go_btn.click()

time.sleep(3)
go_btn_route.click()
from_bar.send_keys("Bucharest")
to_bar.send_keys("Lengerich")
time.sleep(3)
calculate.click()
time.sleep(5)
# distance = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[5]/p[1]")
distance = driver.find_element(By.XPATH, "//*[@id='sidebar_content']/p[1]")
print(distance.text)
driver.quit()
