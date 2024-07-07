from tkinter import *
from colours import *
from helpers import *
from PIL import ImageTk, Image

from pages import DEarProcessPage


class PreviewImagePage(Canvas, BasePage):
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

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data = None):
        self.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/frame4/image_1.png"))
        image_1 = self.create_image(
            566.0,
            378.0,
            image=image_image_1
        )

        captured_img = ImageTk.PhotoImage(Image.open(relative_to_image_capture("test_image.jpg")))
        image_2 = self.create_image(
            566.0,
            292.5,
            image=captured_img
        )

        self.create_text(
            65.0,
            589.0,
            anchor="nw",
            text="Pastikan gambar terlihat dengan jelas dan memiliki posisi sempurna. Jika gambar terlihat kurang sempurna silakan untuk mengambil ulang gambar.",
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("control/frame4/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goToPage(DEarProcessPage.DEarProcessPage(self.window)),
            relief="flat"
        )
        button_1.place(
            x=370.5,
            y=631.0,
            width=192.0,
            height=54.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/frame4/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=570.5,
            y=631.0,
            width=192.0,
            height=54.0
        )

        self.create_text(
            65.0,
            541.0,
            anchor="nw",
            text="Gambar Berhasil Diambil!",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/frame4/image_3.png"))
        image_3 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/frame4/image_4.png"))
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
            font=("SFProText Semibold", 15 * -1))

        self.window.mainloop()