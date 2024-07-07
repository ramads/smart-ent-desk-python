from tkinter import *
from colours import *
from helpers import *

from pages import PatientQueuePage


class HomePage(Canvas, BasePage):

    def __init__(self, window):
        self.window = window
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

    def drawPage(self):
        self.place(x=0, y=0)

        inactive_button_1 = relative_to_assets("control/HomeFrame/button_1.png")
        active_button_1 = relative_to_assets("control/HomeFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/HomeFrame/button_2.png")
        active_button_2 = relative_to_assets("control/HomeFrame/active_button_2.png")

        inactive_button_3 = relative_to_assets("control/HomeFrame/button_3.png")
        active_button_3 = relative_to_assets("control/HomeFrame/active_button_3.png")
        
        inactive_button_4 = relative_to_assets("control/HomeFrame/button_4.png")
        active_button_4 = relative_to_assets("control/HomeFrame/active_button_4.png")
        
        inactive_button_5 = relative_to_assets("control/HomeFrame/button_5.png")
        active_button_5 = relative_to_assets("control/HomeFrame/active_button_5.png")
        
        inactive_button_6 = relative_to_assets("control/HomeFrame/button_6.png")
        active_button_6 = relative_to_assets("control/HomeFrame/active_button_6.png")
        
        create_hover_button(self.window, 47.0, 216.0, 447.0, 319.0, 
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(PatientQueuePage.PatientQueuePage(self.window)))
        
        create_hover_button(self.window, 523.0,216.0, 263.0, 319.0, 
                            BACKGROUND_COLOUR, inactive_button_2, active_button_2,  
                            lambda: print("button_2 clicked"))
        
        create_hover_button(self.window, 815.0,216.0, 271.0, 151.0, 
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: print("button_3 clicked"))
        
        create_hover_button(self.window, 815.0,384.0, 271.0, 151.0, 
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: print("button_4 clicked"))
        
        create_hover_button(self.window, 269.0,591.0, 275.0, 99.0, 
                            BACKGROUND_COLOUR, inactive_button_5, active_button_5,  
                            lambda: print("button_5 clicked"))
        
        create_hover_button(self.window, 590.0,591.0, 274.0, 99.0,
                            BACKGROUND_COLOUR, inactive_button_6, active_button_6,  
                            lambda: print("button__6 clicked"))


        image_image_1 = PhotoImage(
            file=relative_to_assets("control/HomeFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/HomeFrame/image_2.png"))
        image_2 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/HomeFrame/image_3.png"))
        image_3 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_3
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text="RS. Universitas Mataram",
            fill="#FFFFFF",
            font=("Nunito Black", 14 * -1)
        )

        self.create_text(
            130.0,
            144.5,
            anchor="nw",
            text="Unit THT",
            fill="#F1F1F1",
            font=("Nunito SemiBold", 12 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/HomeFrame/image_4.png"))
        image_4 = self.create_image(
            89.0,
            139.0,
            image=image_image_4
        )

        self.window.mainloop()