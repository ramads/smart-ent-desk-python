from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar
from PIL import ImageTk, Image

from pages import DEarResultPage

import json

class FullScreenImagePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.temp_data =temp_data
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.zoom_factor = 1.0

        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
    def drawPage(self, data = None):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_1.png"))

        self.create_image(
            568.0,
            378.0,
            image=image_image_1
        )

        self.image_path = relative_to_image_capture("test_image.jpg")
        self.original_image = Image.open(self.image_path)
        self.original_image = self.original_image.resize((1010, 561))

        self.update_image()


        inactive_button_1 = relative_to_assets(f"control/FullScreenImageFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/FullScreenImageFrame/{self.lang_code}/active_button_1.png")

        inactive_button_2 = relative_to_assets(f"control/FullScreenImageFrame/zoom_in.png")
        active_button_2 = relative_to_assets(f"control/FullScreenImageFrame/active_zoom_in.png")

        inactive_button_3 = relative_to_assets(f"control/FullScreenImageFrame/zoom_out.png")
        active_button_3 = relative_to_assets(f"control/FullScreenImageFrame/active_zoom_out.png")
        
        
        create_hover_button(self.window, 500.5, 648.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_1, active_button_1,
                            lambda: goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data)))

        create_hover_button(self.window, 980.5, 492.0, 52.0, 52.0,
                            "#000000", inactive_button_2, active_button_2,
                            lambda: self.zoom_in())


        create_hover_button(self.window, 980.5, 556.0, 52.0, 52.0,
                            "#000000", inactive_button_3, active_button_3,
                            lambda: self.zoom_out())

        self.window.mainloop()

    def update_image(self):
        # Calculate the new size of the image based on zoom factor
        new_width = int(self.original_image.width * self.zoom_factor)
        new_height = int(self.original_image.height * self.zoom_factor)
        resized_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)

        # Crop the resized image to maintain the 1019x452 ratio
        x_center = new_width // 2
        y_center = new_height // 2
        crop_width, crop_height = 1010, 561
        x1 = max(0, x_center - crop_width // 2)
        y1 = max(0, y_center - crop_height // 2)
        x2 = min(new_width, x_center + crop_width // 2)
        y2 = min(new_height, y_center + crop_height // 2)

        cropped_image = resized_image.crop((x1, y1, x2, y2))

        # Create ImageTk.PhotoImage from the cropped image
        self.captured_img = ImageTk.PhotoImage(cropped_image)

        # Remove the previous image if it exists
        if hasattr(self, 'image_2_id'):
            self.delete(self.image_2_id)

        self.image_2_id = self.create_image(
            568.0,
            351,
            image=self.captured_img
        )

    def zoom_in(self):
        self.zoom_factor *= 1.1
        self.update_image()

    def zoom_out(self):
        self.zoom_factor /= 1.1
        self.update_image()