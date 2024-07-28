from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from PIL import ImageTk, Image

from pages import HomePage, MedicalRecordPage
from pprint import pprint
from datetime import datetime

from database.models.Diagnosis import DiagnosisModel
import json


class DEarCompletePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.temp_data = temp_data
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        pprint(temp_data)
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.diagnosis = DiagnosisModel()
        self.result_dict = {
            'Aerotitis Barotrauma': 'Kondisi yang disebabkan oleh perbedaan tekanan antara telinga tengah dan lingkungan sekitarnya, sering terjadi saat naik atau turun pesawat.',
            'Cerumen': 'Penumpukan kotoran telinga (serumen) yang dapat menyebabkan penyumbatan dan gangguan pendengaran sementara.',
            'Corpus Alienum': 'Benda asing yang masuk dan tersangkut di telinga, sering terjadi pada anak-anak.',
            'M Timpani normal': 'Kondisi gendang telinga yang normal dan sehat, tanpa tanda-tanda infeksi atau kerusakan.',
            'Myringitis Bulosa': 'Infeksi gendang telinga yang menyebabkan pembentukan lepuhan berisi cairan pada permukaannya.',
            'Normal': 'Kondisi telinga yang sehat tanpa adanya tanda-tanda penyakit atau kelainan.',
            'OE Difusa': 'Otitis Eksterna difusa adalah peradangan menyeluruh pada telinga luar, biasanya disebabkan oleh infeksi bakteri atau jamur.',
            'OE Furunkulosa': 'Infeksi telinga luar yang disebabkan oleh abses atau bisul pada saluran telinga luar.',
            'OMA Hiperemis': 'Otitis Media Akut dengan hiperemia, yaitu peradangan telinga tengah yang disertai dengan kemerahan pada gendang telinga.',
            'OMA Oklusi Tuba': 'Otitis Media Akut dengan oklusi tuba, yaitu penyumbatan pada tuba Eustachius yang menghubungkan telinga tengah dengan bagian belakang hidung.',
            'OMA Perforasi': 'Otitis Media Akut yang menyebabkan perforasi atau robekan pada gendang telinga.',
            'OMA Resolusi': 'Otitis Media Akut yang sedang dalam fase penyembuhan, dengan gejala yang mulai berkurang.',
            'OMA Supurasi': 'Otitis Media Akut dengan keluarnya nanah dari telinga tengah.',
            'OMed Efusi': 'Otitis Media dengan efusi, yaitu adanya cairan di telinga tengah tanpa adanya infeksi akut.',
            'OMedK Resolusi': 'Otitis Media Kronis yang sedang dalam fase penyembuhan.',
            'OMedK Tipe Aman': 'Otitis Media Kronis tipe aman, yaitu infeksi telinga tengah kronis yang tidak menimbulkan komplikasi serius.',
            'OMedK Tipe Bahaya': 'Otitis Media Kronis tipe bahaya, yaitu infeksi telinga tengah kronis yang berpotensi menimbulkan komplikasi serius seperti kerusakan tulang atau infeksi otak.',
            'Otomikosis': 'Infeksi telinga yang disebabkan oleh jamur, biasanya terjadi pada telinga luar.',
            'Perforasi Membran Tympani': 'Robekan atau lubang pada gendang telinga yang dapat disebabkan oleh infeksi, trauma, atau tekanan yang tiba-tiba.',
            'Tympanosklerotik': 'Kondisi di mana jaringan parut terbentuk di gendang telinga atau telinga tengah, seringkali sebagai hasil dari infeksi telinga kronis atau berulang.'
        }
        if self.temp_data.get('id_diagnosis'): self.update_data()
        else : self.insert_data()

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data
    
    def update_data(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f"{self.temp_data['id_patient']}_{self.temp_data['id_hospital']}_{timestamp}.png"
        
        image = Image.open(self.temp_data['image_path_temp'])
        image = image.resize((559, 471))
        image.save(f"temp_image/{image_path}", format='PNG')
        
        confidence = self.temp_data['result_1'][1]
        confidence = int(round(confidence, 2) * 100)
        
        self.diagnosis.update_diagnosis(
            id_diagnosis=self.temp_data['id_diagnosis'],
            diagnosis=self.temp_data['result_1'][0],
            diagnosis_date=current_date,
            result=self.result_dict[self.temp_data['result_1'][0]],
            confidence=confidence,
            image_path=image_path,
            is_corrected=self.temp_data['is_corrected'],
            correction_reason=self.temp_data['correction_reason'],
            hospital_id=self.temp_data['id_hospital'],
            patient_id=self.temp_data['id_patient'],
            diagnosis_type=self.temp_data['diagnosis_type']
        )
    def insert_data(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f"{self.temp_data['id_patient']}_{self.temp_data['id_hospital']}_{timestamp}.png"
        
        image = Image.open(self.temp_data['image_path_temp'])
        image = image.resize((559, 471))
        image.save(f"temp_image/{image_path}", format='PNG')
        
        confidence = self.temp_data['result_1'][1]
        confidence = int(round(confidence, 2) * 100)
        
        self.diagnosis.insert_diagnosis(
            diagnosis=self.temp_data['result_1'][0],
            diagnosis_date=current_date,
            result=self.result_dict[self.temp_data['result_1'][0]],
            confidence=confidence,
            image_path=image_path,
            is_corrected=self.temp_data['is_corrected'],
            correction_reason=self.temp_data['correction_reason'],
            hospital_id=self.temp_data['id_hospital'],
            patient_id=self.temp_data['id_patient'],
            diagnosis_type=self.temp_data['diagnosis_type']
        )
        


    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data = None):
        self.place(x = 0, y = 0)

        # wifi_clock_app = notificationBar(self.window)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            377.0,
            image=self.image_image_1
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_4.png"))
        image_4 = self.create_image(
            566.5,
            304.5,
            image=self.image_image_4
        )

        self.create_text(
            1133.0/2,
            472.0,
            anchor="center",
            justify="center",
            text=self.data_localization['diagnosis_complete'].title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1),
        )

        self.create_text(
            1133.0/2,
            520.0,
            anchor="center",
            justify="center",
            text=self.data_localization['diagnosis_complete_hint'],
            fill="#8A8C8F",
            font=("Nunito Regular", 16 * -1)
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()


        self.window.after(2000, self.goToNextPage)
        # self.window.mainloop()

         # Delay for 3 seconds before navigating to the HomePage

    def goToNextPage(self):
        if self.temp_data.get('id_diagnosis'):
            goToPage(MedicalRecordPage.MedicalRecordPage(self.window))
        else:
            goToPage(HomePage.HomePage(self.window))