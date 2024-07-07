from tkinter import *
from colours import *
from helpers import *
from pages.DEarPage import DEarPage

class DiagnosisPage(Canvas, BasePage):
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

    def drawPage(self, data = None):
        self.place(x=0, y=0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goToPage(DEarPage(self.window)),
            relief="flat"
        )
        button_1.place(
            x=41.0,
            y=255.0,
            width=332.0,
            height=319.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=402.0,
            y=255.0,
            width=330.0,
            height=319.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=761.0,
            y=255.0,
            width=332.0,
            height=319.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DiagnosisFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        self.create_text(
            281.0,
            608.0,
            anchor="nw",
            text="Silakan pilih diagnosa yang akan anda lakukan. \nKami akan menyiapkannya untuk anda.",
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