import time

from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.Pages.switch_window import SwitchWindow
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestSwitchWindow(TestCaseModel):
    home = Home()
    switch = SwitchWindow()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_switchwindow()
        self.switch.click_on_open_tab()
        self.home.click_on_switchwindow()
        self.switch.click_open_alert()
        self.switch.accept_allert()


    def tear_down(self):
        self.home.quit_test()

if __name__ == "__main__":
    test = TestSwitchWindow()
    test.setup()
    time.sleep(2)
    test.run()
    time.sleep(2)
    test.tear_down()

