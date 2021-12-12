import time

from PageObjectModel.Pages.file_upload import FileUpload
from PageObjectModel.Pages.homepage import Home
from PageObjectModel.TestCases.test_case_model import TestCaseModel


class TestFileUpload(TestCaseModel):
    home = Home()
    file_up = FileUpload()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_fileupload()
        self.file_up.click_on_choose()
        self.file_up.click_on_reset()

    def tear_down(self):
        self.home.quit_test()


if __name__ == "__main__":
    test = TestFileUpload()
    test.setup()
    time.sleep(3)
    test.run()
    time.sleep(3)
    test.tear_down()
