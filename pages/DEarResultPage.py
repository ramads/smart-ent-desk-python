import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image

from pages import DEarCorrectionPage
from machine_learning.image_predictor import ImagePredictor
from datetime import datetime

from database.models.Diagnosis import DiagnosisModel
from database.models.History import HistoryModel
from database.models.Patient import PatientModel
from database.models.Insurance import InsuranceModel

from pages import DEarCompletePage
from pages import FullScreenImagePage

class DEarResultPage(Canvas, BasePage):
    def __init__(self, window, result_1, result_2, result_3, id_patient=None, organ=None):

        self.window = window
        self.result_1=list(result_1)
        self.result_2=list(result_2)
        self.result_3=list(result_3)

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
        self.organ = organ
        self.diagnosis = DiagnosisModel()
        self.history = HistoryModel()
        self.patient = PatientModel()
        self.insurance = InsuranceModel()

        self.get_patient_data()
        self.get_insurance_data()

    def get_patient_data(self):
        self.patient_data = self.patient.get_patient(self.id_patient)

    def get_insurance_data(self):
        self.insurance_data = self.insurance.get_patient_insurances(self.id_patient)
    
    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))
    
    def insert_data(self, hospital_id, diagnosis, diagnosis_date, result, confidence, image_path_temp):
        history_id = self.history.insert_history(self.id_patient, hospital_id, self.organ)
        image_path = f"temp_image/{self.id_patient}_{history_id}.jpg"
        image = Image.open(image_path_temp)
        image.save(image_path)
        confidence = round(confidence, 2) * 100
        confidence = int(confidence)
        self.diagnosis.insert_diagnosis(history_id, diagnosis, diagnosis_date, result, confidence, image_path)

    def drawPage(self):
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
        resized_image = original_image.resize((600, 335)) 
        captured_img = ImageTk.PhotoImage(resized_image)
        image_2 = self.create_image(
            361.0,
            235.5,
            image=captured_img
        )

        # Initialize the predictor
        print("Pattient ID: ", self.id_patient)
        predictor = ImagePredictor()

        image_path = 'temp_image/test_image.jpg'

        # Get the prediction results
        result_1, result_2, result_3 = predictor.predict(image_path)
        
        current_date = datetime.now().strftime("%Y-%m-%d")

        image_path_temp = image_path
        self.insert_data(1, result_1[0], current_date,"", result_1[1],  image_path_temp)

        # image_image_3 = PhotoImage(
        #     file=relative_to_assets("control/DEarResultFrame/image_3.png"))
        # image_3 = self.create_image(
        #     623.0,
        #     356.0,
        #     image=image_image_3
        # )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarResultFrame/image_4.png"))
        image_4 = self.create_image(
            895.0,
            233.0,
            image=image_image_4
        )

        #pie chart
        labels = [self.result_1[0], self.result_2[0], self.result_3[0], "Lainnya"]
        sizes = [int(self.result_1[1] * 100), int(self.result_2[1] * 100), int(self.result_3[1] * 100), (100-int((self.result_1[1]+ self.result_2[1]+ self.result_3[1])*100))]
        colors = ['lightcoral',  'gold', 'yellowgreen', 'lightskyblue']
        explode = (0.1, 0, 0, 0)

        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%d%%', shadow=True, startangle=140)
        ax.axis('equal')

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        ax.add_artist(centre_circle)

        chart_canvas = FigureCanvasTkAgg(fig, master=self)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().place(x=740.5, y=115.0)

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
            text=self.result_3[0],
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
            text=self.result_2[0],
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
            text=self.result_1[0],
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
            361.0,
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
            text=self.result_1[0],
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
            text = "{} %".format(int(self.result_1[1] * 100)),
            fill="#1E5C2A",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            67.0,
            583.0,
            anchor="nw",
            text="Note: Jika hasil diagnosa dirasa keliru, silakan untuk melakukan koreksi hasil.",
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
            text="Informasi Pasien",
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
            text="No Asuransi     : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
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
            text="Jenis Asuransi  : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
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
            text="Kelas Asuransi : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
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
            text="Fasilitas Kesehatan : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            890.0,
            615.0,
            anchor="nw",
            text=self.insurance_data[0]['fasilitas_kesehatan'],
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

        inactive_button_1 = relative_to_assets("control/DEarResultFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DEarResultFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/DEarResultFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DEarResultFrame/active_button_2.png")
        
        inactive_button_3 = relative_to_assets("control/DEarResultFrame/button_3.png")
        active_button_3 = relative_to_assets("control/DEarResultFrame/active_button_3.png")

        create_hover_button(self.window, 597.0, 330.0, 52.0, 52.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(FullScreenImagePage.FullScreenImagePage(self.window, self.result_1, self.result_2, self.result_3)))
        
        create_hover_button(self.window, 67.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_2, active_button_2, 
                            lambda: goToPage(DEarCorrectionPage.DEarCorrectionPage(self.window, self.result_1, self.result_2, self.result_3)))
        
        create_hover_button(self.window, 267.0, 623.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_3, active_button_3,  
                            lambda: goToPage(DEarCompletePage.DEarCompletePage(self.window)))


        self.window.mainloop()