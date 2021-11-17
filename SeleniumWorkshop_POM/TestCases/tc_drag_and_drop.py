import time

from SeleniumWorkshop_POM.Pages.drag_and_drop import DragAndDrop
from SeleniumWorkshop_POM.Pages.homepage import Home
from SeleniumWorkshop_POM.TestCases.test_case_model import TestCaseModel


class TestDragAndDrop(TestCaseModel):
    home = Home()
    drag_and_drop = DragAndDrop()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_drag_and_drop()
        self.drag_and_drop.click_on_image()
        self.drag_and_drop.drag_image_on_box()

    def tear_down(self):
        self.home.quit_test()


if __name__ == "__main__":
    test = TestDragAndDrop()
    test.setup()
    time.sleep(3)
    test.run()
    time.sleep(3)
    test.tear_down()
