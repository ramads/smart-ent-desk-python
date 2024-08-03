from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import DEarPage
from pages import DiagnosisPage

from pprint import pprint

from database.models.MedicalFacility import HospitalModel
from config import DUMMY_HOSPITAL
import json


class DiagnosisQuestionPage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.hospital_data = HospitalModel().get_hospital(DUMMY_HOSPITAL)
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.temp_data = temp_data

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def create_checkbox_components(self, num_components):
        initial_x = 230.5
        initial_y = 330.0
        x_offset = 200
        max_width = 1100    # Maksimal lebar frame checkbox
        current_x = initial_x
        current_y = initial_y

        self.vars = []  # Ini output checkbox, simpan di db

        for i in range(num_components):
            if current_x + x_offset > max_width:
                current_x = initial_x
                current_y += 50

            var = IntVar()
            self.vars.append(var)

            # Buat kolom checkbox
            checkbox = Checkbutton(
                self,
                variable=var,
                command=self.update_selected_options,
                bg="white",  # Set background color to white
                highlightthickness=0,
                relief="flat"
            )
            checkbox.place(
                x=current_x,
                y=current_y,
                anchor="nw"
            )

            # Buat Text
            self.create_text(
                current_x + 25,  # Atur posisi text di kanan
                current_y,
                anchor="nw",
                text=f"Option {i + 1}",
                fill="#404040",  # Text color
                font=("Nunito Regular", 16 * -1)
            )

            current_x += x_offset

    def update_selected_options(self):
        selected_options = [i + 1 for i, var in enumerate(self.vars) if var.get()]
        print("Selected options:", selected_options)

    def drawPage(self, data=None):
        self.place(x=0, y=0)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_2.png"))
        image_2 = self.create_image(
            571.0,
            414.0,
            image=image_image_2
        )

        inactive_continue = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/active_continue.png")
        active_continue = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/inactive_continue.png")

        create_hover_button(self.window, 575.0, 614.0, 136.0, 42.0,
                            "#FFFFFF", inactive_continue, active_continue,
                            lambda: goToPage(DEarPage.DEarPage(self.window, self.temp_data, "telinga")))

        inactive_back = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/inactive_back.png")
        active_back = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/active_back.png")

        create_hover_button(self.window, 430.0, 614.0, 136.0, 42.0,
                            "#FFFFFF", inactive_back, active_back,
                            lambda: goToPage(DiagnosisPage.DiagnosisPage(self.window)))

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_3.png"))
        image_3 = self.create_image(
            571.0,
            522.0,
            image=image_image_3
        )

        # Atur jumlah check box
        self.create_checkbox_components(7)

        # Text area
        entry_1 = TextArea(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            placeholder="You can fill more detail here (optional) ..."
        )

        entry_1.place(
            x=150.0,
            y=475.0,
            width=840.0,
            height=95.0
        )

        self.create_text(
            1133/2.0,
            190.0,
            anchor="center",
            justify="center",
            text=self.data_localization["question_title"],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            1133/2.0,
            250.5,
            anchor="center",
            justify="center",
            width=800,
            text=self.data_localization["question_description"],
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()

        # self.window.after(2000, self.goToNextPage)  # Delay
        self.window.mainloop()
