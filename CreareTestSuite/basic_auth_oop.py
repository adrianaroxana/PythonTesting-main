import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuth(unittest.TestCase):
    auth_btn = (By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("D:/AUTOMATION TESTING COURSE/PythonTesting-main/SeleniumWorkshop_POM/Resources/chromedriver.exe")
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_auth(self):
        self.driver.find_element(*self.auth_btn).click()
        user = "admin"
        pwd = "admin"
        self.driver.get("https://" + user + ":" + pwd + "@the-internet.herokuapp.com/basic_auth")
        self.driver.back()  # pt fiecare instanta de driver deschisa
        self.driver.back()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
