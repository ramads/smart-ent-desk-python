from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image

from pages import DEarProcessPage
from pages import DEarLoadingPage


class PreviewImagePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
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
        self.temp_data = temp_data

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data = None):
        self.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/PreviewImageFrame/image_1.png"))
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
            560.0,
            600.0,
            anchor="center",
            text="Pastikan gambar terlihat dengan jelas dan memiliki posisi sempurna. Silakan untuk mengambil ulang gambar jika belum jelas.",
            fill="#8A8C8F",
            font=("Nunito Regular", 15 * -1)
        )


        inactive_button_1 = relative_to_assets("control/PreviewImageFrame/button_1.png")
        active_button_1 = relative_to_assets("control/PreviewImageFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/PreviewImageFrame/button_2.png")
        active_button_2 = relative_to_assets("control/PreviewImageFrame/active_button_2.png")
        
        create_hover_button(self.window, 370.5, 631.0, 192.0, 54.0, 
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DEarProcessPage.DEarProcessPage(self.window, self.temp_data)))
        create_hover_button(self.window, 570.5, 631.0, 192.0, 54.0, 
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: goToPage(DEarLoadingPage.DEarLoadingPage(self.window, self.temp_data)))



        self.create_text(
            565.0,
            550.0,
            anchor="center",
            text="Gambar Berhasil Diambil!",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/PreviewImageFrame/image_3.png"))
        image_3 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/PreviewImageFrame/image_4.png"))
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