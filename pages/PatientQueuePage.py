import customtkinter
import tkinter as tk
from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import DiagnosisPage
from pages import HomePage
from pages import EndQueuePage
from pages import MedicalRecordDetailPage

from database.models.Patient import PatientModel
from database.models.Diagnosis import DiagnosisModel
from database.models.Insurance import InsuranceModel
from database.models.Hospital import HospitalModel

import json
from config import DUMMY_HOSPITAL


class PatientQueuePage(Canvas, BasePage):
    def __init__(self, window):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.window = window
        self.current_patient = 0
        self.initialize_models()
        self.hospital_data = self.hospital.get_hospital(DUMMY_HOSPITAL)
        self.get_patient_data()
        self.get_patient_insurance()
        self.get_disease_title()

    def get_disease_title(self):
        if self.lang_code == "id":
            self.disease_title_1 = f"{self.data_localization['disease']} {self.data_localization[self.current_history_data[0]['jenis_diagnosa']]}" if len(self.current_history_data)>0 else self.data_localization['no_data_yet']
            self.disease_title_2 = f"{self.data_localization['disease']} {self.data_localization[self.current_history_data[1]['jenis_diagnosa']]}" if len(self.current_history_data)>1 else self.data_localization['no_data_yet']
        else:
            self.disease_title_1 = f"{self.data_localization[self.current_history_data[0]['jenis_diagnosa']]} {self.data_localization['disease']}" if len(self.current_history_data)>0 else self.data_localization['no_data_yet']
            self.disease_title_2 = f"{self.data_localization[self.current_history_data[1]['jenis_diagnosa']]} {self.data_localization['disease']}" if len(self.current_history_data)>1 else self.data_localization['no_data_yet']

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data


    def initialize_models(self):
        self.patient = PatientModel()
        self.diagnosis = DiagnosisModel()
        self.insurance = InsuranceModel()
        self.hospital = HospitalModel()

    def get_patient_data(self):
        self.patient_data = self.patient.get_all_patients()
        if self.patient_data:
            self.get_current_patient_data()

    def get_current_patient_data(self):
        self.current_history_data = self.diagnosis.get_patient_diagnoses(self.patient_data[self.current_patient]['id_pasien'])
        self.get_patient_insurance()

    def get_patient_insurance(self):
        self.patient_insurance = self.insurance.get_patient_insurances(self.patient_data[self.current_patient]['id_pasien'])

    def next_patient(self):
        if self.current_patient < len(self.patient_data) - 1:
            self.current_patient += 1
            self.get_current_patient_data()
            self.drawPage()
        else:
            goToPage(EndQueuePage.EndQueuePage(self.window))
    

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))
    

    def drawPage(self, data = None):
        self.place(x = 0, y = 0)

        # wifi_clock_app = notificationBar(self.window)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets(f"control/PatientQueueFrame/image_1.png"))
        image_1 = self.create_image(
            382.0,
            405.0,
            image=self.image_image_1
        )

        self.create_text(
            86.0,
            219.5,
            anchor="nw",
            text=self.patient_data[self.current_patient]['nama_pasien'],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            86.0,
            278.5,
            anchor="nw",
            text=f"{self.data_localization['gender']}\t: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            278.5,
            anchor="nw",
            text=self.patient_data[self.current_patient]['jenis_kelamin'],
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            312.5,
            anchor="nw",
            text=f"{self.data_localization['date_of_birth']}\t: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            312.5,
            anchor="nw",
            text=self.patient_data[self.current_patient]['tanggal_lahir'].strftime("%d %B %Y"),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            346.5,
            anchor="nw",
            text=f"{self.data_localization['address']}\t\t: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            346.5,
            anchor="nw",
            text=self.patient_data[self.current_patient]['alamat'],
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            380.5,
            anchor="nw",
            text=f"{self.data_localization['last_diagnosis']}\t: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            257.0,
            384.5,
            anchor="nw",
            text= " " * 4 + self.current_history_data[0]['diagnosa'] if self.current_history_data and self.current_history_data[0]['diagnosa'] else self.data_localization['no_data_yet'],
            fill="#1E5C2A",
            font=("Nunito Bold", 19 * -1)
        )
        
        text_widget = tk.Text(self.window, wrap="word", font=("Nunito regular", 12), bg="#FFFFFF", fg="#404040", bd=0, highlightthickness=0)
        text_widget.place(x=86, y=417.5, width=600, height=150)  # ukuran box

        # Mengisi teks ke Text Widget
        if self.current_history_data and len(self.current_history_data) > 0:
            text_content = self.current_history_data[0]['hasil_diagnosa'] or self.data_localization['no_data_yet']
        else:
            text_content = self.data_localization['no_data_yet']
        text_widget.insert(tk.END, text_content)

        text_widget.tag_configure("justify", justify="left")
        text_widget.tag_add("justify", "1.0", "end")

        # Menonaktifkan Text Widget agar tidak dapat diedit
        text_widget.configure(state="disabled")

        self.image_image_2 = PhotoImage(
            file=relative_to_assets(f"control/PatientQueueFrame/image_2.png"))
        image_2 = self.create_image(
            897.0,
            339.0,
            image=self.image_image_2
        )

        # Tampilan Asuransi

        self.image_image_7 = PhotoImage(
            file=relative_to_assets(f"control/PatientQueueFrame/image_7.png"))
        image_7 = self.create_image(
            897.0,
            592.0,
            image=self.image_image_7
        )

        self.create_text(
            752.0,
            520.0,
            anchor="nw",
            text=f"{self.data_localization['insurance']}".title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            752.0,
            570.0,
            anchor="nw",
            text=f"{self.data_localization['insurance_number']}: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            900.0,
            570.0,
            anchor="nw",
            text=self.patient_insurance[0]['nomor_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            594.0,
            anchor="nw",
            text=f"{self.data_localization['insurance_type']}: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            900.0,
            594.0,
            anchor="nw",
            text=self.patient_insurance[0]['jenis_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            618.0,
            anchor="nw",
            text=f"{self.data_localization['insurance_class']}: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            900.0,
            618.0,
            anchor="nw",
            text=self.patient_insurance[0]['kelas_asuransi'],
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            642.0,
            anchor="nw",
            text=f"{self.data_localization['medical_facility']}: ".capitalize(),
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            900.0,
            642.0,
            anchor="nw",
            text=self.patient_insurance[0]['fasilitas_kesehatan'],
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets(f"control/PatientQueueFrame/image_8.png"))
        image_8 = self.create_image(
            566.0,
            89.0,
            image=self.image_image_8
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text=self.hospital_data['nama_rumah_sakit'],
            fill="#FFFFFF",
            font=("Nunito Black", 14 * -1)
        )

        self.create_text(
            130.0,
            144.5,
            anchor="nw",
            text=self.data_localization['ent_unit'],
            fill="#F1F1F1",
            font=("Nunito SemiBold", 12 * -1)
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets(f"control/PatientQueueFrame/image_9.png"))
        image_9 = self.create_image(
            89.0,
            139.0,
            image=self.image_image_9
        )

        inactive_button_3 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/button_3.png")
        active_button_3 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/active_button_3.png")
        
        inactive_button_4 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/active_button_4.png")
        
        inactive_button_5 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/button_5.png")
        active_button_5 = relative_to_assets(f"control/PatientQueueFrame/{self.lang_code}/active_button_5.png")

        create_hover_button(self.window, 59.5, 633.5, 192.0, 54.0, 
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: goToPage(HomePage.HomePage(self.window)))
                            # lambda: [self.destroy_all_widgets, goToPage(HomePage.HomePage(self.window))])


        create_hover_button(self.window, 284.5, 633.5, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: goToPage(DiagnosisPage.DiagnosisPage(self.window, self.patient_data[self.current_patient]['id_pasien'])))
        
        create_hover_button(self.window, 509.5, 633.5, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_5, active_button_5,  
                            lambda: self.next_patient())

        # Kolom riwayat penyakit
        self.create_text(
            752.0,
            224.0,
            anchor="nw",
            text=f"{self.data_localization['medical_record']}".title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=300,
                                                         height=200,
                                                         fg_color="#FFFFFF",
                                                         scrollbar_button_hover_color="#404040",
                                                         scrollbar_fg_color="#FFFFFF",
                                                         bg_color="#FFFFFF",
                                                         border_width=0)

        self.my_frame.place(x=740, y=255)
        self.canvas_scroll = Canvas(self.my_frame,
                                    width=300,
                                    height=500,
                                    bg="#FFFFFF",
                                    highlightthickness=0,
                                    borderwidth=0)
        self.canvas_scroll.pack()

        self.update_cards()

    def update_cards(self):
        self.canvas_scroll.delete("all")

        button_images = []
        location_images = []
        schedule_images = []

        for i in range(len(self.current_history_data)):
            y_offset = i * 75
            self.current_history_data[i]['nama_pasien'] = self.patient_data[self.current_patient]['nama_pasien']

            # button_image_1 = PhotoImage(file=relative_to_assets(f"control/PatientQueueFrame/link_button.png"))
            # button_images.append(button_image_1)
            # button_1 = Button(self.canvas_scroll, background="white", activebackground="white", image=button_image_1, borderwidth=0, highlightthickness=0,
            #                   command=lambda i=i: goToPage(MedicalRecordDetailPage.MedicalRecordDetailPage(self.window, self.current_history_data[i], "patient_queue")),
            #                   relief="flat")

            inactive_link_button = relative_to_assets(f"control/PatientQueueFrame/link_button.png")
            active_link_button = relative_to_assets(f"control/PatientQueueFrame/active_link_button.png")

            button_1 = create_hover_button(self.canvas_scroll, 0, 0, 0, 0,
                                "#FFFFFF", inactive_link_button, active_link_button,
                                lambda i=i: goToPage(MedicalRecordDetailPage.MedicalRecordDetailPage(self.window, self.current_history_data[i], PatientQueuePage)))

            self.canvas_scroll.create_window(240, 15 + y_offset, anchor="nw", window=button_1,
                                             width=44, height=44)

            self.canvas_scroll.create_text(
                0,
                0 + y_offset,
                anchor="nw",
                text=self.disease_title_1.title(),
                fill="#404040",
                font=("Nunito Bold", 19 * -1)
            )

            self.canvas_scroll.create_text(
                30,
                27 + y_offset,
                anchor="nw",
                text=self.current_history_data[i]['diagnosa'],
                fill="#404040",
                font=("Nunito Regular", 11 * -1)
            )

            self.image_image_3 = PhotoImage(
                file=relative_to_assets(f"control/PatientQueueFrame/image_3.png"))
            schedule_images.append(self.image_image_3)
            image_3 = self.canvas_scroll.create_image(
                10,
                35 + y_offset,
                image=self.image_image_3
            )

            self.image_image_4 = PhotoImage(
                file=relative_to_assets(f"control/PatientQueueFrame/image_4.png"))
            schedule_images.append(self.image_image_4)
            image_4 = self.canvas_scroll.create_image(
                10,
                55 + y_offset,
                image=self.image_image_4
            )

            self.canvas_scroll.create_text(
                30,
                50.0 + y_offset,
                anchor="nw",
                text=self.hospital.get_hospital(self.current_history_data[i]['id_rumah_sakit'])['nama_rumah_sakit'],
                fill="#404040",
                font=("Nunito Regular", 11 * -1)
            )



        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))

        # self.window.mainloop()
