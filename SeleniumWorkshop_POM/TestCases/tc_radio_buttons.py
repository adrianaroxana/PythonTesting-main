import time

from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.Pages.radio_button import RadioButton
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestRadioButton(TestCaseModel):
    home = Home()
    radio_btn = RadioButton()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_radio_button()
        time.sleep(2)
        self.radio_btn.click_on_radio_button1()
        time.sleep(2)
        self.radio_btn.click_on_radio_button2()
        time.sleep(2)
        self.radio_btn.click_on_radio_button3()

    def tear_down(self):
        self.home.quit_test()

if __name__ == "__main__":
    test = TestRadioButton()
    test.setup()
    test.run()
    test.tear_down()