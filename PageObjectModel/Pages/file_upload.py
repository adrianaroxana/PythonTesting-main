from PageObjectModel.driver import Driver


class FileUpload(Driver):
    CHOOSE = "Choose"
    RESET = "Reset"


    def click_on_choose(self):
        print(f"Click on the element with selector {self.CHOOSE}")

    def click_on_reset(self):
        print(f"Click on the element with selector {self.RESET}")