from PageObjectModel.driver import Driver


class Navbar(Driver):
    FORMY_HOME = "logo"
    FORM = "Form"
    COMPONENTS = "navbarDropdownMenuLink"

    def click_on_navbar(self):
        print(f"Click on element with selector {self.FORMY_HOME}")

    def click_on_form(self):
        print(f"Click on element with selector {self.FORM}")

    def click_on_components(self):
        print(f"Click on element with selector {self.COMPONENTS}")
