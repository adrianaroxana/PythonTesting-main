from SeleniumWorkshop_POM.driver import Driver


class RadioButton(Driver):

    RADIOBUTTON1 = "radio-button-1"
    RADIOBUTTON2 = "radio-button-2"
    RADIOBUTTON3 = "radio-button-3"


    def click_on_radio_button1(self):
        print(f"Click on the element with selector {self.RADIOBUTTON1}")

    def click_on_radio_button2(self):
        print(f"Click on the element with selector {self.RADIOBUTTON2}")

    def click_on_radio_button3(self):
        print(f"Click on the element with selector {self.RADIOBUTTON3}")