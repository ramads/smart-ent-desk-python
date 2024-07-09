from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image
from tkinter import ttk

from pages import DEarResultPage


class DEarCorrectionPage(Canvas, BasePage):
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
            file=relative_to_assets("control/DEarCorrectionFrame/image_1.png"))
        image_1 = self.create_image(
            376.0,
            378.0,
            image=image_image_1
        )

        image_path = relative_to_image_capture("test_image.jpg")
        original_image = Image.open(image_path)
        resized_image = original_image.resize((604, 600))  # Resize to 604x538
        captured_img = ImageTk.PhotoImage(resized_image)
        image_2 = self.create_image(
            370.0,
            377.5,
            image=captured_img
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/image_3.png"))
        image_3 = self.create_image(
            904.0,
            295.0,
            image=image_image_3
        )

        self.create_text(
            749.0,
            75.0,
            anchor="nw",
            text="Koreksi Hasil",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            749.0,
            123.0,
            anchor="nw",
            text="Untuk mengoreksi hasil diagnosa \n sebelumnya, mohon untuk memilih label\n berikut yang dinilai sesuai dengan penyakit \n yang diderita pasien dan sertakan \nalasan yang jelas.",
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            749.0,
            227.0,
            anchor="nw",
            text="Label Baru",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        def show():
            label = clicked.get()
            print(clicked.get())
            goToPage(DEarResultPage.DEarResultPage(self.window))

        # Define options
        options = [
            'Aerotitis Barotrauma', 'Cerumen', 'Corpus Alienum', 'M Timpani normal', 
            'Myringitis Bulosa', 'Normal', 'OE Difusa', 'OE Furunkulosa', 'OMA Hiperemis', 
            'OMA Oklusi Tuba', 'OMA Perforasi', 'OMA Resolusi', 'OMA Supurasi', 'OMed Efusi', 
            'OMedK Resolusi', 'OMedK Tipe Aman', 'OMedK Tipe Bahaya', 'Otomikosis', 
            'Perforasi Membran Tympani', 'Tympanosklerotik'
        ]

        # Create a Tkinter StringVar to hold the selected option
        clicked = StringVar()
        clicked.set("options[0]")

        # Create a style for the OptionMenu
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Rounded.TMenubutton",
                        relief="flat",
                        padding=6,
                        background="#FFFFFF",
                        foreground="black",
                        borderwidth=1,
                        bordercolor="black",
                        border=8,
                        focusthickness=3,
                        focuscolor="#FFFFFF",
                        anchor="w")
        style.map("Rounded.TMenubutton",
                background=[("active", "skyblue")])
        

        # Create the OptionMenu with the custom style
        drop = ttk.OptionMenu(self.window, clicked, options[0], *options)
        drop.config(style="Rounded.TMenubutton")
        drop.pack(pady=20)

        drop.place(
            x=749.0,
            y=262.0,
            width=310.0,
            height=40.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=show,
            relief="flat"
        )
        button_3.place(
            x=908.0,
            y=463.0,
            width=150.0,
            height=46.0
        )

        self.create_text(
            749.0,
            334.0,
            anchor="nw",
            text="Alasan",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/entry_1.png"))
        entry_bg_1 = self.create_image(
            904.0,
            404.0,
            image=entry_image_1
        )
        entry_1 = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=759.0,
            y=368.0,
            width=290.0,
            height=70.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goToPage(DEarResultPage.DEarResultPage(self.window)),
            relief="flat"
        )
        button_2.place(
            x=750.0,
            y=463.0,
            width=150.0,
            height=46.0
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/image_4.png"))
        image_4 = self.create_image(
            1099.3330078125,
            22.33349609375,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/DEarCorrectionFrame/image_5.png"))
        image_5 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_5
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.window.mainloop()