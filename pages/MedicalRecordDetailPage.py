import customtkinter
from tkinter import *
from colors import *
from helpers import *
from notificationBar import notificationBar


from pages import MedicalRecordPage

from database.models.Diagnosis import DiagnosisModel

from config import LANG_CODE
import json


class MedicalRecordDetailPage(Canvas, BasePage):

    def __init__(self, window):
        self.window = window
        self.dignosisModel = DiagnosisModel()
        self.temp_data = self.dignosisModel.get_patient_joint_diagnoses()
        self.history_data = self.temp_data
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

    def get_localization(self):
        path = f"locales/{LANG_CODE}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def drawPage(self):
        self.place(x=0, y=0)

        wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        inactive_button_3 = relative_to_assets("control/MedicalRecordDetailFrame/button_3.png")
        active_button_3 = relative_to_assets("control/MedicalRecordDetailFrame/active_button_3.png")

        inactive_button_4 = relative_to_assets("control/MedicalRecordDetailFrame/button_4.png")
        active_button_4 = relative_to_assets("control/MedicalRecordDetailFrame/active_button_4.png")

        create_hover_button(self.window, 1008.0, 563.0, 52.0, 52.0,
                            "#000000", inactive_button_3, active_button_3,
                            lambda: print("button clicked"))

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,
                            lambda: goToPage(MedicalRecordPage.MedicalRecordPage(self.window)))


        image_image_2 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_2.png"))
        image_2 = self.create_image(
            262.0,
            389.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_3.png"))
        image_3 = self.create_image(
            792.0,
            389.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_4.png"))
        image_4 = self.create_image(
            262.0,
            247.5,
            image=image_image_4
        )

        text_widget = tk.Text(self.window, wrap="word", font=("Nunito Regular", 12), bg="#FFFFFF", fg="#404040", bd=0,
                              highlightthickness=0)
        text_widget.place(x=72, y=525, width=380, height=100)

        text_content = "OMA Perofrasi adalah gangguan adalah gangguan adalah gangguan adalah gangguan adalah gangguan ........ . Dicirikan dengan .......Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. ",
        text_widget.insert(tk.END, text_content)

        text_widget.tag_configure("justify", justify="left")
        text_widget.tag_add("justify", "1.0", "end")

        # Menonaktifkan Text Widget agar tidak dapat diedit
        text_widget.configure(state="disabled")

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_5.png"))
        image_5 = self.create_image(
            790.0,
            388.0,
            image=image_image_5
        )


        self.create_text(
            288.0,
            492.0,
            anchor="nw",
            text="65%",
            fill="#1E5C2A",
            font=("Nunito Bold", 16 * -1)
        )

        self.create_text(
            72.0,
            492.0,
            anchor="nw",
            text="Tingkat keyakinan dignosa : ",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            257.0,
            455.0,
            anchor="nw",
            text="OMA PERFORASI",
            fill="#1E5C2A",
            font=("Nunito Bold", 19 * -1)
        )

        self.create_text(
            72.0,
            455.0,
            anchor="nw",
            text="Hasil Diagnosa            :",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            257.0,
            421.0,
            anchor="nw",
            text="Selasa, 16 April 2024",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            72.0,
            421.0,
            anchor="nw",
            text="Tanggal Pemeriksaan : ",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            72.0,
            362.0,
            anchor="nw",
            text="Alma Liakua Mutia",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.window.mainloop()

