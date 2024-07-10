from tkinter import *
from colors import *
from helpers import *
from pages.DEarPage import DEarPage

class DiagnosisPage(Canvas, BasePage):
    def __init__(self, window, id_patient = None):
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
        self.id_patient = id_patient

    def drawPage(self, data = None):
        self.place(x=0, y=0)

        inactive_button_1 = relative_to_assets("control/DiagnosisFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DiagnosisFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/DiagnosisFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DiagnosisFrame/active_button_2.png")

        inactive_button_3 = relative_to_assets("control/DiagnosisFrame/button_3.png")
        active_button_3 = relative_to_assets("control/DiagnosisFrame/active_button_3.png")
        
        create_hover_button(self.window, 41.0, 255.0, 332.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(DEarPage(self.window, self.id_patient, "Telinga")))
        
        create_hover_button(self.window, 402.0, 255.0, 330.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_2, active_button_2,  
                            lambda: print("button_2 clicked"))
        
        create_hover_button(self.window, 761.0, 255.0, 332.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: print("button_3 clicked"))

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        self.create_text(
            555.0,
            630.0,
            anchor="center",
            text="Silakan pilih diagnosa yang akan anda lakukan.\n      Kami akan menyiapkannya untuk anda.",
            fill="#FFFFFF",
            font=("Nunito SemiBold", 16 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/image_2.png"))
        image_2 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/image_3.png"))
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
            file=relative_to_assets("control/DiagnosisFrame/image_4.png"))
        image_4 = self.create_image(
            89.0,
            139.0,
            image=image_image_4
        )

        self.window.mainloop()