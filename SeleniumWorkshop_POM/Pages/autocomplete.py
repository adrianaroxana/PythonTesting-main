from SeleniumWorkshop_POM.driver import Driver


class Autocomplete(Driver):
    ADDRESS = "autocomplete"
    STREET_ADDRESS = "street_number"
    STREET_ADDRESS2 = "route"
    CITY = "locality"
    STATE = "administrative_area_level_1"
    ZIP_CODE = "postal_code"
    COUNTRY = "country"

    def click_on_address(self):
        print(f"Click on element with selector{self.ADDRESS}")

    def click_on_street_address(self):
        print(f"Click on element with selector{self.STREET_ADDRESS}")

    def click_on_street_address2(self):
        print(f"Click on element with selector{self.STREET_ADDRESS2}")

    def click_on_city(self):
        print(f"Click on element with selector{self.CITY}")

    def click_on_state(self):
        print(f"Click on element with selector{self.STATE}")

    def click_on_zipcode(self):
        print(f"Click on element with selector{self.ZIP_CODE}")

    def click_on_country(self):
        print(f"Click on element with selector{self.COUNTRY}")
