from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from PIL import Image

from pages import HomePage, MedicalRecordPage
from pprint import pprint
from datetime import datetime

from database.models import MedicalRecord, PatientMedicalFacility, Disease, MedicalRecordIndication
import json
import os
from config import DUMMY_MEDICAL_FACILITY



class CompletePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.temp_data = temp_data
        self.initialize_models()
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

        if self.temp_data.get('id_rekam_medis'):
            self.update_data()
        else:
            self.insert_data()

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data
    
    def initialize_models(self):
        self.medical_record = MedicalRecord.MedicalRecordModel()
        self.patient_medical_facility = PatientMedicalFacility.PatientMedicalFacilityModel()
        self.disease = Disease.DiseaseModel()
        self.medical_record_indication = MedicalRecordIndication.MedicalRecordIndicationModel()

    def get_disease_id(self, nama_penyakit, diagnosis_type):
        return self.disease.get_disease_id(nama_penyakit, organ_penyakit=diagnosis_type)['id_penyakit']
    
    def update_data(self):
        if not os.path.exists(os.path.join("images", self.temp_data['diagnosis_type'])):
            os.makedirs(os.path.join("images", self.temp_data['diagnosis_type']))
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f"{self.temp_data['NIK']}_{self.temp_data['id_faskes']}_{timestamp}.png"
        image_path = os.path.join(self.temp_data['diagnosis_type'], image_path)
        
        image = Image.open(self.temp_data['image_path_temp'])
        image = image.resize((512, 512))
        image.save(f"images/{image_path}", format='PNG')
        
        confidence = self.temp_data['result_1'][1]
        confidence = int(round(confidence, 2) * 100)
        
        self.medical_record.update_medical_record(
            id_rekam_medis=self.temp_data['id_rekam_medis'],
            tanggal_pemeriksaan=current_datetime,
            tingkat_keyakinan=confidence,
            prediksi_benar=self.temp_data['is_corrected'],
            alasan_koreksi=self.temp_data['correction_reason'],
            gambar_penyakit=image_path,
            NIK=self.temp_data['NIK'],
            id_faskes=self.temp_data['id_faskes'],
            id_penyakit=self.get_disease_id(self.temp_data['result_1'][0], self.temp_data['diagnosis_type']),
            deskripsi_gejala=self.temp_data['detail'] if self.temp_data.get('detail') else None
        )

        self.medical_record_indication.delete_medical_record_indication_by_medical_record(id_rekam_medis=self.temp_data['id_rekam_medis'])
        if self.temp_data.get('indications'):
            for indication in self.temp_data['indications']:
                self.medical_record_indication.insert_medical_record_indication(
                    id_rekam_medis=self.temp_data['id_rekam_medis'],
                    id_gejala=indication[0]
                )

    def insert_data(self):
        if not os.path.exists(os.path.join("images", self.temp_data['diagnosis_type'])):
            os.makedirs(os.path.join("images", self.temp_data['diagnosis_type']))

        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f"{self.temp_data['NIK']}_{self.temp_data['id_faskes']}_{timestamp}.png"
        image_path = os.path.join(self.temp_data['diagnosis_type'], image_path)

        image = Image.open(self.temp_data['image_path_temp'])
        image = image.resize((512, 512))
        image.save(f"images/{image_path}", format='PNG')
        
        confidence = self.temp_data['result_1'][1]
        confidence = int(round(confidence, 2) * 100)
        
        id_medical_record =  self.medical_record.insert_medical_record(
            tanggal_pemeriksaan=current_datetime,
            tingkat_keyakinan=confidence,
            prediksi_benar=self.temp_data['is_corrected'],
            alasan_koreksi=self.temp_data['correction_reason'],
            gambar_penyakit=image_path,
            NIK=self.temp_data['NIK'],
            id_faskes=self.temp_data['id_faskes'],
            id_penyakit=self.get_disease_id(self.temp_data['result_1'][0], self.temp_data['diagnosis_type']),
            deskripsi_gejala=self.temp_data['detail'] if self.temp_data.get('detail') else None
        )

        # Update Queue
        # self.patient_medical_facility.update_queue(
        #     status_periksa='selesai',
        #     NIK=self.temp_data['NIK'],
        #     id_faskes=self.temp_data['id_faskes'],
        #     tanggal_pendaftaran=self.temp_data['tanggal_pendaftaran']
        # )

        if self.temp_data.get('indications'):
            for indication in self.temp_data['indications']:
                self.medical_record_indication.insert_medical_record_indication(
                    id_rekam_medis=id_medical_record,
                    id_gejala=indication[0]
                )

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data=None):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarCompleteFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            377.0,
            image=image_image_1
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

        self.window.after(2000, self.goToNextPage)  # Delay
        self.window.mainloop()

    def goToNextPage(self):
        if self.temp_data.get('id_diagnosis'):
            goToPage(MedicalRecordPage.MedicalRecordPage(self.window))
        else:
            goToPage(HomePage.HomePage(self.window))
