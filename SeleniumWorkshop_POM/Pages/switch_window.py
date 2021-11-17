from SeleniumWorkshop_POM.driver import Driver


class SwitchWindow(Driver):

    OPEN_TAB = "new-tab-button"
    OPEN_ALERT = "alert_button"


    def click_on_open_tab(self):
        print(f"Click on the element with selector {self.OPEN_TAB}")

    def click_open_alert(self):
        print(f"Click on the element with selector {self.OPEN_ALERT}")

    def accept_allert(self):
        print("Click ok on allert")