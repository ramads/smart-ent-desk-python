import customtkinter
from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar


from pages import HomePage
from pages import MedicalRecordDetailPage
from pages import MedicalRecordEditPage

from database.models import MedicalRecord, Disease, MedicalFacility

from config import DUMMY_MEDICAL_FACILITY
import json
from pprint import pprint


class MedicalRecordPage(Canvas, BasePage):

    def __init__(self, window, temp_data=None):
        self.window = window
        self.initialize_models()
        self.get_histories_data()
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

        self.drawPage()

    def initialize_models(self):
        self.medical_record = MedicalRecord.MedicalRecordModel()
        self.disease = Disease.DiseaseModel()
        self.medical_facility = MedicalFacility.MedicalFacilityModel()

    def get_histories_data(self):
        self.temp_data = self.medical_record.get_medical_record_join_disease_join_patient()
        self.history_data = self.temp_data

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def searching(self):
        input_text = self.searchingBox.get("1.0", "end-1c").lower().strip()
        input_text = input_text.replace("\n", "").replace("\t", "").replace(" ", "")
        print(input_text)
        if input_text == "" or input_text == "enteryourtexthere..." or input_text == "masukkanteksandadisini...":
            self.history_data = self.temp_data
        else:
            self.history_data = [
                item for item in self.temp_data if input_text in item['nama_pasien'].lower().replace(" ", "")
            ]

        self.update_cards()

    def delete_diagnosis(self, id_rekam_medis):
        self.medical_record.delete_medical_record(id_rekam_medis)
        self.get_histories_data()
        self.update_cards()

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            413.0,
            image=image_image_1
        )

        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=955,
                                                         height=300,
                                                         fg_color="#FFFFFF",
                                                         scrollbar_button_hover_color="#404040",
                                                         scrollbar_fg_color="#F3F3F3",
                                                         bg_color="#FFFFFF",
                                                         border_width=0)

        self.my_frame.place(x=75, y=312)
        self.canvas_scroll = Canvas(self.my_frame,
                                    width=955,
                                    height=2000,
                                    bg="#FFFFFF",
                                    highlightthickness=0,
                                    borderwidth=0)
        self.canvas_scroll.pack()

        self.create_text(
            81.0,
            280.0,
            anchor="nw",
            text=self.data_localization['name'].title(),
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            380,
            280.0,
            anchor="nw",
            text=self.data_localization['diagnosis'].title(),
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            650.0,
            280.0,
            anchor="nw",
            text=self.data_localization['check_date'].title(),
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            915.0,
            280.0,
            anchor="nw",
            text=self.data_localization['action'].title(),
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_4.png"))
        image_4 = self.create_image(
            566.0,
            89.0,
            image=image_image_4
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text=self.medical_facility.get_medical_facility(DUMMY_MEDICAL_FACILITY)['nama_faskes'],
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

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_5.png"))
        image_5 = self.create_image(
            89.0,
            139.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_6.png"))
        image_6 = self.create_image(
            764.0,
            239.0,
            image=image_image_6
        )

        self.create_text(
            81.0,
            216.0,
            anchor="nw",
            text=self.data_localization['patient_history'].title(),
            fill="#404040",
            font=("Nunito Bold", 25 * -1)
        )

        self.searchingBox = TextArea(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito Bold", 12),
            placeholder=self.data_localization["enter_text"]
        )
        self.searchingBox.place(
            x=611.0,
            y=230.0,
            width=300.0,
            height=30.0
        )

        inactive_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/active_button_4.png")

        inactive_button_5 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/button_5.png")
        active_button_5 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/active_button_5.png")

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,
                            lambda: goToPage(HomePage.HomePage(self.window)))

        create_hover_button(self.window, 940.0, 216.0, 120.0, 45.0,
                            "#FFFFFF", inactive_button_5, active_button_5,
                            lambda: self.searching())

        self.update_cards()

    def update_cards(self):
        self.canvas_scroll.delete("all")

        button_images = []

        for i in range(len(self.history_data)):
            y_offset = i * 50
            self.canvas_scroll.create_rectangle(81.0, 367.0 + y_offset, 1278.0, 367.0 + y_offset,
                                                fill="#F3F3F3", outline="")
            self.canvas_scroll.create_text(81.0, 331.0 + y_offset, anchor="nw",
                                           text=self.history_data[i]['nama_pasien'],
                                           fill="#404040",
                                           font=("Nunito Regular", 18 * -1))
            self.canvas_scroll.create_text(380, 331.0 + y_offset, anchor="nw",
                                           text=self.history_data[i]['nama_penyakit'],
                                           fill="#404040",
                                           font=("Nunito Regular", 18 * -1))
            self.canvas_scroll.create_text(650, 331.0 + y_offset, anchor="nw",
                                           text=self.history_data[i]['tanggal_pemeriksaan'].strftime("%d %B %Y"),
                                           fill="#404040",
                                           font=("Nunito Regular", 16 * -1))

            button_image_1 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/edit_button.png"))
            button_images.append(button_image_1)
            button_1 = Button(self.canvas_scroll, image=button_image_1, borderwidth=0, highlightthickness=0,
                              background="#FFFFFF",
                              command=lambda i=i: goToPage(MedicalRecordEditPage.MedicalRecordEditPage(self.window, self.history_data[i])), relief="flat")
            self.canvas_scroll.create_window(914.22119140625, 329.20361328125 + y_offset, anchor="nw", window=button_1,
                                             width=23.592920303344727, height=23.592920303344727)

            button_image_2 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/view_button.png"))
            button_images.append(button_image_2)
            button_2 = Button(self.canvas_scroll, image=button_image_2, borderwidth=0, highlightthickness=0,
                              background="#FFFFFF",
                              command=lambda i=i: goToPage(MedicalRecordDetailPage.MedicalRecordDetailPage(self.window, self.history_data[i], MedicalRecordPage)), relief="flat")
            self.canvas_scroll.create_window(942.814208984375, 329.20361328125 + y_offset, anchor="nw", window=button_2,
                                             width=23.592920303344727, height=23.592920303344727)

            button_image_3 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/button_3.png"))
            button_images.append(button_image_3)
            button_3 = Button(self.canvas_scroll, image=button_image_3, borderwidth=0, highlightthickness=0,
                              background="#FFFFFF", command=lambda i=i: self.delete_diagnosis(self.history_data[i]['id_rekam_medis']), relief="flat")
            self.canvas_scroll.create_window(971.406982421875, 329.20361328125 + y_offset, anchor="nw", window=button_3,
                                             width=23.592920303344727, height=23.592920303344727)

        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        self.window.mainloop()
