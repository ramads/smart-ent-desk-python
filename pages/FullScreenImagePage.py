from tkinter import *
from colors import *
from helpers import *
from notificationBar import notificationBar
from PIL import ImageTk, Image

from pages import DEarResultPage

class FullScreenImagePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.temp_data =temp_data
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

        wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_1.png"))

        image_1 = self.create_image(
            568.0,
            378.0,
            image=image_image_1
        )

        image_path = relative_to_image_capture("test_image.jpg")
        original_image = Image.open(image_path)
        resized_image = original_image.resize((1010, 561))  # Resize to 604x538
        captured_img = ImageTk.PhotoImage(resized_image)

        image_2 = self.create_image(
            568.0,
            351,
            image=captured_img
        )

        inactive_button_1 = relative_to_assets("control/FullScreenImageFrame/button_1.png")
        active_button_1 = relative_to_assets("control/FullScreenImageFrame/active_button_1.png")
        
        
        create_hover_button(self.window, 500.5, 648.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data)))

        
        self.window.mainloop()