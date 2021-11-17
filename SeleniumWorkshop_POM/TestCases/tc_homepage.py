import time

from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.Pages.navbar import Navbar
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestHomepage(TestCaseModel):
    home = Home()
    navbar_home = Navbar()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_autocomplete()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_buttons()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_checkbox()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_datepicker()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_drag_and_drop()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_drop_down()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_enabled_and_disabled_elements()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_fileupload()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_key_mouse_press()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_modal()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_page_scroll()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_radio_button()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_switchwindow()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)
        self.home.click_on_complete_web_form()
        time.sleep(2)
        self.navbar_home.click_on_navbar()
        time.sleep(2)


    def tear_down(self):
        self.home.quit_test()


if __name__ == "__main__":
    test = TestHomepage()
    test.setup()
    test.run()
    test.tear_down()