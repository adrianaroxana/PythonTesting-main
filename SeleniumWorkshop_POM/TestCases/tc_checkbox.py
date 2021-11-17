import time

from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.Pages.checkbox import Checkbox
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestCheckbox(TestCaseModel):
    home = Home()
    checkbox = Checkbox()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_checkbox()
        time.sleep(2)
        self.checkbox.click_on_checkbox1()
        time.sleep(2)
        self.checkbox.click_on_checkbox2()
        time.sleep(2)
        self.checkbox.click_on_checkbox3()


    def tear_down(self):
        self.home.quit_test()

if __name__ == "__main__":
    test = TestCheckbox()
    test.setup()
    test.run()
    test.tear_down()




