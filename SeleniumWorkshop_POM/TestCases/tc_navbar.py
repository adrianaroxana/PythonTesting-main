import time

from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.Pages.navbar import Navbar
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestNavbar(TestCaseModel):
    home = Home()
    nav = Navbar()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.nav.click_on_navbar()
        self.nav.click_on_form()
        self.nav.click_on_components()

    def tear_down(self):
        self.home.quit_test()



if __name__ == "__main__":
    test = TestNavbar()
    test.setup()
    time.sleep(2)
    test.run()
    time.sleep(3)
    test.tear_down()
