from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image

from pages import HomePage


class DEarCompletePage(Canvas, BasePage):
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
        self.place(x = 0, y = 0)
        
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            377.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_2.png"))
        image_2 = self.create_image(
            1099.3330078125,
            22.33349609375,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_3.png"))
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

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_4.png"))
        image_4 = self.create_image(
            566.5,
            304.5,
            image=image_image_4
        )

        self.create_text(
            1133.0/2,
            472.0,
            anchor="center",
            text="Proses Diagnosis Selesai",
            fill="#404040",
            font=("Nunito Bold", 24 * -1),
        )

        self.create_text(
            1133.0/2,
            520.0,
            anchor="center",
            text="Diagnosis berhasil dilakukan. Hasil diagnosis dapat di akses kembali pada menu riwayat pasien.",
            fill="#8A8C8F",
            font=("Nunito Regular", 16 * -1)
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()


        self.window.after(2000, self.go_to_homepage)
        self.window.mainloop()

         # Delay for 3 seconds before navigating to the HomePage

    def go_to_homepage(self):
        goToPage(HomePage.HomePage(self.window))