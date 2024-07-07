from tkinter import *
from colours import *
from helpers import *
from pages.DiagnosisPage import DiagnosisPage


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
        button_image_1 = PhotoImage(
            file=relative_to_assets("control/frame8/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goToPage(DiagnosisPage(self.window)),
            relief="flat"
        )
        button_1.place(
            x=47.0,
            y=216.0,
            width=447.0,
            height=319.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/frame8/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=523.0,
            y=216.0,
            width=263.0,
            height=319.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("control/frame8/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=815.0,
            y=216.0,
            width=271.0,
            height=151.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("control/frame8/button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=815.0,
            y=384.0,
            width=271.0,
            height=151.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("control/frame8/button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=269.0,
            y=591.0,
            width=275.0,
            height=99.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("control/frame8/button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=590.0,
            y=591.0,
            width=274.0,
            height=99.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/frame8/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/frame8/image_2.png"))
        image_2 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/frame8/image_3.png"))
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
            file=relative_to_assets("control/frame8/image_4.png"))
        image_4 = self.create_image(
            89.0,
            139.0,
            image=image_image_4
        )

        self.window.mainloop()