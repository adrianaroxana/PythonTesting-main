from PageObjectModel.Pages.autocomplete import Autocomplete
from PageObjectModel.Pages.homepage import Home
from PageObjectModel.TestCases.test_case_model import TestCaseModel
import time

class TestAutocomplete(TestCaseModel):
    home = Home()
    auto = Autocomplete()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_autocomplete()
        time.sleep(3)
        self.auto.click_on_address()
        time.sleep(3)
        self.auto.click_on_street_address()
        time.sleep(3)
        self.auto.click_on_street_address2()
        time.sleep(3)
        self.auto.click_on_city()
        time.sleep(3)
        self.auto.click_on_state()
        time.sleep(3)
        self.auto.click_on_zipcode()
        time.sleep(3)
        self.auto.click_on_country()
        time.sleep(3)

    def tear_down(self):
        self.home.quit_test()



if __name__ == '__main__':
    test1 = TestAutocomplete()
    test1.setup()
    time.sleep(4)
    test1.run()
    time.sleep(4)
    test1.tear_down()
