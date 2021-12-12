import time

from PageObjectModel.Pages.datepicker import DatePicker
from PageObjectModel.Pages.homepage import Home
from PageObjectModel.TestCases.test_case_model import TestCaseModel


class TestDatepicker(TestCaseModel):
    home = Home()
    datepkr = DatePicker()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_datepicker()
        time.sleep(2)
        self.datepkr.click_on_date()
        time.sleep(2)
        self.datepkr.click_on_day()
        time.sleep(2)

    def tear_down(self):
        self.home.quit_test()


if __name__ == "__main__":
    test = TestDatepicker()
    test.setup()
    time.sleep(3)
    test.run()
    time.sleep(3)
    test.tear_down()