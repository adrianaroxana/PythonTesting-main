from SeleniumWorkshop_POM.driver import Driver


class Home(Driver):
    AUTOCOMPLETE = "Autocomplete"
    BUTTONS = "Buttons"
    CHECKBOX = "Checkbox"


    def click_on_autocomplete(self):
        print(f"Click on button with locator {self.AUTOCOMPLETE}")

    def click_on_buttons(self):
        print(f"Click on button with locator {self.BUTTONS}")

    def click_on_checkbox(self):
        print(f"Click on button with locator {self.CHECKBOX}")