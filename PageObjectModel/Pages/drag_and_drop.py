from PageObjectModel.driver import Driver


class DragAndDrop(Driver):
    IMAGE = "image"
    DROP_BOX = "box"

    def click_on_image(self):
        print(f"Click on element with selector {self.IMAGE}")

    def drag_image_on_box(self):
        print(f"Drag element with selctor {self.IMAGE} on element with selector {self.DROP_BOX}")


