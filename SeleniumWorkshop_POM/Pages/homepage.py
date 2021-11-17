from SeleniumWorkshop_POM.driver import Driver


class Home(Driver):
    AUTOCOMPLETE = "Autocomplete"
    BUTTONS = "Buttons"
    CHECKBOX = "Checkbox"
    DATEPICKER = "Datepicker"
    DRAG_AND_DROP = "Drag and Drop"
    DROPDOWN = "Dropdown"
    ENABLED_DISABLED = "Enabled and disabled elements"
    FILEUPLOAD = "File Upload"
    KEY_MOUSE_PRESS = "Key and Mouse Press"
    MODAL = "Modal"
    PAGE_SCROLL = "Page Scroll"
    RADIO_BUTTON = "Radio Button"
    SWITCH_WINDOW = "Switch Window"
    COMPLETE_FORM = "Complete Web Form"


    def click_on_autocomplete(self):
        print(f"Click on element with selector {self.AUTOCOMPLETE}")

    def click_on_buttons(self):
        print(f"Click on element with selector {self.BUTTONS}")

    def click_on_checkbox(self):
        print(f"Click on element with selector {self.CHECKBOX}")

    def click_on_datepicker(self):
        print(f"Click on element with selector {self.DATEPICKER}")

    def click_on_drag_and_drop(self):
        print(f"Click on element with selector {self.DRAG_AND_DROP}")

    def click_on_drop_down(self):
        print(f"Click on element with selector {self.DROPDOWN}")

    def click_on_enabled_and_disabled_elements(self):
        print(f"Click on element with selector {self.ENABLED_DISABLED}")

    def click_on_fileupload(self):
        print(f"Click on element with selector {self.FILEUPLOAD}")

    def click_on_key_mouse_press(self):
        print(f"Click on element with selector {self.KEY_MOUSE_PRESS}")

    def click_on_modal(self):
        print(f"Click on element with selector {self.MODAL}")

    def click_on_page_scroll(self):
        print(f"Click on element with selector {self.PAGE_SCROLL}")

    def click_on_radio_button(self):
        print(f"Click on element with selector {self.RADIO_BUTTON}")

    def click_on_switchwindow(self):
        print(f"Click on element with selector {self.SWITCH_WINDOW}")

    def click_on_complete_web_form(self):
        print(f"Click on element with selector {self.COMPLETE_FORM}")

