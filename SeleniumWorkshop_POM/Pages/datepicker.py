from SeleniumWorkshop_POM.driver import Driver


class DatePicker(Driver):

    DATEPICKER = "datepicker"
    DAY = "1636588800000"

    def click_on_date(self):
        print(f"Click on the element with selector {self.DATEPICKER}")

    def click_on_day(self):
        print(f"Click on the element with selector {self.DAY}")