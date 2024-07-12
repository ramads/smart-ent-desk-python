from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image
from tkinter import ttk
from notificationBar import notificationBar

from pages import DEarResultPage


class DEarCorrectionPage(Canvas, BasePage):
    def __init__(self, window, temp_data):
        self.window = window
        self.temp_data = temp_data
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

        wifi_clock_app = notificationBar(self.window)

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
            375.0,
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
            text="Untuk mengoreksi hasil diagnosa sebelumnya, mohon untuk memilih label berikut yang dinilai sesuai dengan penyakit yang diderita pasien dan sertakan alasan yang jelas.",
            fill="#8A8C8F",
            font=("Nunito Regular", 14 * -1),
            width=320
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
            self.temp_data['result_1'] = (label, self.temp_data['result_1'][1])
            self.temp_data['is_corrected'] = False
            self.temp_data['correction_reason'] = entry_1.get("1.0", "end-1c")
            goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data))

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
        clicked.set("Pilih Label")

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

        entry_1 = TextArea(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            placeholder="Enter your text here..."
        )
        entry_1.place(
            x=758.0,
            y=372.0,
            width=290.0,
            height=65.0
        )

        inactive_button_2 = relative_to_assets("control/DEarCorrectionFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DEarCorrectionFrame/active_button_2.png")

        inactive_button_3 = relative_to_assets("control/DEarCorrectionFrame/button_3.png")
        active_button_3 = relative_to_assets("control/DEarCorrectionFrame/active_button_3.png")

        create_hover_button(self.window, 750.0, 463.0, 150.0, 46.0,
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data)))
        
        create_hover_button(self.window, 908.0, 463.0, 150.0, 46.0,
                            "#FFFFFF", inactive_button_3, active_button_3,  
                            show)


        self.window.mainloop()