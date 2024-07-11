from tkinter import *
from colors import *
from helpers import *

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
        
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_1.png"))

        image_1 = self.create_image(
            568.0,
            378.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_2.png"))
        image_2 = self.create_image(
            560.0,
            351.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_3.png"))
        image_3 = self.create_image(
            1099.3330078125,
            22.33349609375,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/FullScreenImageFrame/image_4.png"))
        image_4 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_4
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        inactive_button_1 = relative_to_assets("control/FullScreenImageFrame/button_1.png")
        active_button_1 = relative_to_assets("control/FullScreenImageFrame/active_button_1.png")
        
        
        create_hover_button(self.window, 500.5, 648.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data)))

        
        self.window.mainloop()