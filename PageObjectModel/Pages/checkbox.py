from PageObjectModel.driver import Driver


class Checkbox(Driver):
    CHECKBOX1 = "checkbox-1"
    CHECKBOX2 = "checkbox-2"
    CHECKBOX3 = "checkbox-3"

    def click_on_checkbox1(self):
        print(f"Click on the element with selector {self.CHECKBOX1}")

    def click_on_checkbox2(self):
        print(f"Click on the element with selector {self.CHECKBOX2}")

    def click_on_checkbox3(self):
        print(f"Click on the element with selector {self.CHECKBOX3}")