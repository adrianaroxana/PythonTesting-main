import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestContext(unittest.TestCase):
    context_menu = (By.CSS_SELECTOR, "#content > ul > li:nth-child(7) > a")
    context_btn = (By.ID, "hot-spot")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("/PageObjectModel/Resources/chromedriver.exe")
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_context(self):
        self.driver.find_element(*self.context_menu).click()
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.context_btn)).perform() # right click on element
        time.sleep(3)
        self.driver.switch_to.alert.dismiss()  #close the alert
        time.sleep(3)