from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import DiagnosisStartPage
from pages import DiagnosisPage

from database.models import Indication
from pprint import pprint

import json
import customtkinter as ctk

class DiagnosisQuestionPage(Canvas, BasePage):
    def __init__(self, window, temp_data=None, diagnosis_type=None, previous_page=None):
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

        self.temp_data = temp_data
        if diagnosis_type:
            self.temp_data["diagnosis_type"] = diagnosis_type

        if previous_page:
            self.temp_data["previous_page"] = previous_page

        self.indication_model = Indication.IndicationModel()
        self.indication_data = self.indication_model.get_indication_by_organ(self.temp_data["diagnosis_type"])
        self.get_disease_title(self.temp_data['diagnosis_type'])

    def get_disease_title(self, disease):
        if self.lang_code == 'id':
            self.disease_title = f"{self.data_localization['disease']} {self.data_localization[disease]}"
        else:
            self.disease_title = f"{self.data_localization[disease]} {self.data_localization['disease']}"

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def create_checkbox_components(self, num_components):
        initial_x = 200.5
        initial_y = 330.0
        x_offset = 200
        max_width = 1100  # Maksimal lebar frame checkbox
        current_x = initial_x
        current_y = initial_y

        self.vars = []  # Ini output checkbox, simpan di db

        for i in range(num_components):
            if current_x + x_offset > max_width:
                current_x = initial_x
                current_y += 50

            var = IntVar()
            self.vars.append((self.indication_data[i]["id_gejala"], self.indication_data[i][f"nama_gejala_{self.lang_code}"], var))

            checkbox = ctk.CTkCheckBox(
                self,
                variable=var,
                command=self.update_selected_options,
                text=self.indication_data[i][f"nama_gejala_{self.lang_code}"],
                font=("Nunito Regular", 16),  # Atur ukuran font untuk memperbesar checkbox
                text_color="#404040",
                checkbox_width=25,  # Atur lebar checkbox
                checkbox_height=25,  # Atur tinggi checkbox
                bg_color="white",
                hover_color="#757575",
                fg_color="#85C13D"
            )
            checkbox.place(
                x=current_x,
                y=current_y,
                anchor="nw"
            )

            current_x += x_offset

    def convert_to_one_hot(self):
        total_unique_values = len([indication["nama_gejala_id"] for indication in self.indication_data])
        data = [indication[1] for indication in self.temp_data["indications"]] if "indications" in self.temp_data else []
        unique_values = []
        for value in self.indication_data:
            unique_values.append(value[f"nama_gejala_{self.lang_code}"])
        value_to_index = {value: idx for idx, value in enumerate(unique_values)}

        one_hot = [0] * total_unique_values
        for value in data:
            one_hot[value_to_index[value]] = 1
        
        self.temp_data["indications_one_hot"] = np.array(one_hot).reshape(1, -1)
        
    def update_selected_options(self):
        selected_options = [ (id_gejala, nama_gejala) for id_gejala, nama_gejala, var in self.vars if var.get() == 1]
        print("Selected options:", selected_options)
        self.temp_data['indications'] = selected_options

    def get_entry_text(self):
        self.temp_data['detail'] = self.entry_1.get("1.0", "end-1c") if self.entry_1.get("1.0", "end-1c") != "You can fill more detail here (optional) ..." else ""

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
                            lambda: [self.convert_to_one_hot(), self.get_entry_text(), goToPage(DiagnosisStartPage.DiagnosisStartPage(self.window, self.temp_data))])

        inactive_back = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/inactive_back.png")
        active_back = relative_to_assets(f"control/DiagnosisQuestionFrame/{self.lang_code}/active_back.png")

        create_hover_button(self.window, 430.0, 614.0, 136.0, 42.0,
                            "#FFFFFF", inactive_back, active_back,
                            lambda: goToPage(self.temp_data['previous_page'](self.window, self.temp_data)))

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_3.png"))
        image_3 = self.create_image(
            571.0,
            522.0,
            image=image_image_3
        )

        # Atur jumlah check box
        self.create_checkbox_components(len(self.indication_data))

        # Text area
        self.entry_1 = TextArea(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            placeholder="You can fill more detail here (optional) ..."
        )

        self.entry_1.place(
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
            text=self.disease_title.title(),
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
