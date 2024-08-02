import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from colors import *
from helpers import *

# from notificationBar import notificationBar

from PIL import ImageTk, Image

from pages import DEarCorrectionPage

from database.models.Patient import PatientModel
from database.models.Insurance import InsuranceModel

from pages import DEarCompletePage
from pages import FullScreenImagePage

from pprint import pprint
import json


class DEarResultPage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):

        self.window = window
        self.temp_data = temp_data
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.patient = PatientModel()
        self.insurance = InsuranceModel()
        self.get_patient_data()
        self.get_insurance_data()
        pprint(self.temp_data)
    
    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def get_patient_data(self):
        self.patient_data = self.patient.get_patient(self.temp_data['id_patient'])
        pprint(self.patient_data)

    def get_insurance_data(self):
        self.insurance_data = self.insurance.get_patient_insurances(self.temp_data['id_patient'])
    
    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_1.png"))
        image_1 = self.create_image(
            361.0,
            233.0,
            image=image_image_1
        )
        
        image_path = relative_to_image_capture("test_image.jpg")
        original_image = Image.open(image_path)
        resized_image = original_image.resize((600, 335)) 
        captured_img = ImageTk.PhotoImage(resized_image)
        image_2 = self.create_image(
            361.0,
            235.5,
            image=captured_img
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_4.png"))
        image_4 = self.create_image(
            895.0,
            233.0,
            image=image_image_4
        )

        # #pie chart
        sizes = [int(self.temp_data['result_1'][1] * 100), int(self.temp_data['result_2'][1] * 100),
                 int(self.temp_data['result_3'][1] * 100), (100-int((self.temp_data['result_1'][1]
                                                                     + self.temp_data['result_2'][1]
                                                                     + self.temp_data['result_3'][1])*100))]

        colors = ['lightcoral',  'gold', 'yellowgreen', 'lightskyblue']
        explode = (0.1, 0, 0, 0)

        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)
        ax.pie(sizes, explode=explode, colors=colors,
               autopct='%d%%', shadow=True, startangle=140)
        ax.axis('equal')

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        ax.add_artist(centre_circle)

        # fig.savefig('pie_chart.png')

        chart_canvas = FigureCanvasTkAgg(fig, master=self)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().place(x=740.5, y=100.0)

        plt.close('all')

        self.create_text(
            726.0,
            300.0,
            anchor="nw",
            text=self.data_localization['graph_information'],
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            726.0,
            75.0,
            anchor="nw",
            text=self.data_localization['picture_analysis'],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_5.png"))
        image_5 = self.create_image(
            910.0,
            377.0,
            image=image_image_5
        )

        self.create_text(
            933.0,
            370.0,
            anchor="nw",
            # text=self.temp_data['result_2'][0],
            text=self.data_localization['other_accumulations'],
            fill="#404040",
            font=("Nunito Regular", 12 * -1),
            width=150
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_6.png"))
        image_6 = self.create_image(
            735.0,
            380,
            image=image_image_6
        )

        self.create_text(
            759.0,
            373.0,
            anchor="nw",
            text=self.temp_data['result_3'][0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        self.create_text(
            933.0,
            329.0,
            anchor="nw",
            text=self.temp_data['result_2'][0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1),
            width=150
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_7.png"))
        image_7 = self.create_image(
            910.0,
            343.0,
            image=image_image_7
        )

        self.create_text(
            758.0,
            329.0,
            anchor="nw",
            text=self.temp_data['result_1'][0],
            fill="#404040",
            font=("Nunito Regular", 12 * -1),
            width=100
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_8.png"))
        image_8 = self.create_image(
            735.0,
            343.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_9.png"))
        image_9 = self.create_image(
            361.0,
            568.0,
            image=image_image_9
        )

        self.create_text(
            67.0,
            459.0,
            anchor="nw",
            text=self.data_localization['diagnosis_result'],
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.create_text(
            67.0,
            507.0,
            anchor="nw",
            text=self.temp_data['result_1'][0],
            fill="#1E5C2A",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            67.0,
            547.0,
            anchor="nw",
            text=self.data_localization['confidence_level'],
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            280.0,
            547.0,
            anchor="nw",
            text="{} %".format(int(self.temp_data['result_1'][1] * 100)),
            fill="#1E5C2A",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            67.0,
            583.0,
            anchor="nw",
            text=self.data_localization['diagnosis_note'],
            fill="#8A8C8F",
            font=("Nunito Bold", 12 * -1)
        )

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
            text=self.data_localization['information_patient'].title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            509.0,
            anchor="nw",
            text=self.patient_data['nama_pasien'],
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            726.0,
            543.0,
            anchor="nw",
            text=f"{self.data_localization['gender_type'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            900.0,
            543.0,
            anchor="nw",
            text=self.insurance_data[0]['nomor_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            567.0,
            anchor="nw",
            text=f"{self.data_localization['latest_diagnose'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            900.0,
            567.0,
            anchor="nw",
            text=self.insurance_data[0]['jenis_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            591.0,
            anchor="nw",
            text=f"{self.data_localization['medical_facility'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            900.0,
            591.0,
            anchor="nw",
            text=self.insurance_data[0]['kelas_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            615.0,
            anchor="nw",
            text=f"{self.data_localization['patient_address'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            900.0,
            615.0,
            anchor="nw",
            text=self.insurance_data[0]['fasilitas_kesehatan'],
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        inactive_button_1 = relative_to_assets("control/DEarResultFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DEarResultFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/DEarResultFrame/{self.lang_code}/button_2.png")
        active_button_2 = relative_to_assets(f"control/DEarResultFrame/{self.lang_code}/active_button_2.png")
        
        inactive_button_3 = relative_to_assets(f"control/DEarResultFrame/{self.lang_code}/button_3.png")
        active_button_3 = relative_to_assets(f"control/DEarResultFrame/{self.lang_code}/active_button_3.png")

        create_hover_button(self.window, 597.0, 330.0, 52.0, 52.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(FullScreenImagePage.FullScreenImagePage(self.window, self.temp_data)))
        
        create_hover_button(self.window, 67.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_2, active_button_2, 
                            lambda: goToPage(DEarCorrectionPage.DEarCorrectionPage(self.window, self.temp_data)))
        
        create_hover_button(self.window, 267.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_3, active_button_3,  
                            lambda: goToPage(DEarCompletePage.DEarCompletePage(self.window, self.temp_data)))

        self.window.mainloop()
        self.destroy()
