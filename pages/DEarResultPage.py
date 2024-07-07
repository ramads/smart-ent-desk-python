from tkinter import *
from colours import *
from helpers import *
from PIL import ImageTk, Image

from pages import DEarProcessPage
from pages import DEarCorrectionPage
from machine_learning.image_predictor import ImagePredictor


class DEarResultPage(Canvas, BasePage):
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
            file=relative_to_assets("control/DEarResultFrame/image_1.png"))
        image_1 = self.create_image(
            361.0,
            233.0,
            image=image_image_1
        )
        
        image_path = relative_to_image_capture("test_image.jpg")
        original_image = Image.open(image_path)
        resized_image = original_image.resize((604, 345))  # Resize to 604x538
        captured_img = ImageTk.PhotoImage(resized_image)
        image_2 = self.create_image(
            341.0,
            215.5,
            image=captured_img
        )

        # Initialize the predictor
        predictor = ImagePredictor()

        image_path = 'temp_image/test_image.jpg'

        # Get the prediction results
        result_1, result_2, result_3 = predictor.predict(image_path)

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_3.png"))
        image_3 = self.create_image(
            623.0,
            356.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_4.png"))
        image_4 = self.create_image(
            895.0,
            233.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_5.png"))
        image_5 = self.create_image(
            895.5,
            215.0,
            image=image_image_5
        )

        self.create_text(
            726.0,
            324.0,
            anchor="nw",
            text="Keterangan grafik:",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            726.0,
            75.0,
            anchor="nw",
            text="Analisa Gambar:",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            1018.0,
            366.5,
            anchor="nw",
            text=result_3[0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_6.png"))
        image_6 = self.create_image(
            996.0,
            378.0,
            image=image_image_6
        )

        self.create_text(
            886.0,
            366.5,
            anchor="nw",
            text=result_2[0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_7.png"))
        image_7 = self.create_image(
            864.0,
            378.0,
            image=image_image_7
        )

        self.create_text(
            754.0,
            366.5,
            anchor="nw",
            text=result_1[0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_8.png"))
        image_8 = self.create_image(
            732.0,
            378.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_9.png"))
        image_9 = self.create_image(
            351.0,
            568.0,
            image=image_image_9
        )

        self.create_text(
            67.0,
            459.0,
            anchor="nw",
            text="Hasil Diagnosa",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.create_text(
            67.0,
            507.0,
            anchor="nw",
            text=result_1[0],
            fill="#1E5C2A",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            67.0,
            547.0,
            anchor="nw",
            text = "Tingkat keyakinan diagnosa: ",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            280.0,
            547.0,
            anchor="nw",
            text = "{} %".format(int(result_1[1] * 100)),
            fill="#1E5C2A",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            67.0,
            583.0,
            anchor="nw",
            text="Note: Jika hasil diagnosa dirasa keliru, silakan untuk melakukan koreksi hasil.",
            fill="#151920",
            font=("Nunito Bold", 12 * -1)
        )

        inactive_button_1 = relative_to_assets("control/DEarResultFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DEarResultFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/DEarResultFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DEarResultFrame/active_button_2.png")
        
        inactive_button_3 = relative_to_assets("control/DEarResultFrame/button_3.png")
        active_button_3 = relative_to_assets("control/DEarResultFrame/active_button_3.png")

        create_hover_button(self.window, 607.0, 340.0, 31.0, 31.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: print("button_1 clicked"))
        
        create_hover_button(self.window, 67.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_2, active_button_2, 
                            lambda: goToPage(DEarCorrectionPage.DEarCorrectionPage(self.window)))
        
        create_hover_button(self.window, 267.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_3, active_button_3,  
                            lambda: print("button_3 clicked"))

        image_image_10 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_10.png"))
        image_10 = self.create_image(
            895.0,
            570.0,
            image=image_image_10
        )

        self.create_text(
            726.0,
            459.0,
            anchor="nw",
            text="Informasi Pasien",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            509.0,
            anchor="nw",
            text="Alma Liakua Mutia",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            726.0,
            543.0,
            anchor="nw",
            text="No Asuransi     : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            839.0,
            543.0,
            anchor="nw",
            text="000863002321023",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            567.0,
            anchor="nw",
            text="Jenis Asuransi  : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            838.0,
            567.0,
            anchor="nw",
            text="BPJS",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            591.0,
            anchor="nw",
            text="Kelas Asuransi : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            838.0,
            591.0,
            anchor="nw",
            text="Kelas 1",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            615.0,
            anchor="nw",
            text="Fasilitas Kesehatan : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            865.0,
            615.0,
            anchor="nw",
            text="Puskesmas Selaparang",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        image_image_11 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_11.png"))
        image_11 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_11
        )

        image_image_12 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_12.png"))
        image_12 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_12
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