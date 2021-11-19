import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMultipleTabs(unittest.TestCase):
    multiple_tabs = (By.CSS_SELECTOR, "#content > ul > li:nth-child(33) > a")
    click_here_btn = (By.CSS_SELECTOR, "#content > div > a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("D:/AUTOMATION TESTING COURSE/PythonTesting-main/SeleniumWorkshop_POM/Resources/chromedriver.exe")
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()

    def test_multiple_tabs(self):
        self.driver.find_element(*self.multiple_tabs).click()
        self.driver.find_element(*self.click_here_btn).click()
        one = self.driver.window_handles[0]
        two = self.driver.window_handles[1]
        i = 0
        while i < 100:
            self.driver.switch_to.window(one)
            self.driver.switch_to.window(two)
            i += 1
            print(i)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()