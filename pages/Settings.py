import customtkinter
from tkinter import *
from colors import *
from helpers import *
from notificationBar import notificationBar


from pages import HomePage

from database.models.Diagnosis import DiagnosisModel

from config import LANG_CODE
import json


class Settings(Canvas, BasePage):

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
            file=relative_to_assets("control/SettingsFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            390.0,
            image=image_image_1
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_4.png"))
        image_4 = self.create_image(
            566.0,
            89.0,
            image=image_image_4
        )

        self.create_text(
            77.0,
            184.0,
            anchor="nw",
            text="Settings",
            fill="#000000",
            font=("Nunito SemiBold", 25 * -1)
        )

        inactive_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{LANG_CODE}/button_4.png")
        active_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{LANG_CODE}/active_button_4.png")

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,
                            lambda: goToPage(HomePage.HomePage(self.window)))


        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=955,
                                                         height=380,
                                                         fg_color="#FFFFFF",
                                                         scrollbar_button_hover_color="#404040",
                                                         scrollbar_fg_color="#F3F3F3",
                                                         bg_color="#FFFFFF",
                                                         border_width=0)

        self.my_frame.place(x=75, y=230)
        self.canvas_scroll = Canvas(self.my_frame, width=955, height=1560, bg="#FFFFFF")
        self.canvas_scroll.pack()


        self.update_cards()

    def update_cards(self):
        self.canvas_scroll.delete("all")

        button_images = []

        # for i in range(len(self.history_data)):
        #     y_offset = i * 50

        self.canvas_scroll.create_text(
            121.0,
            249.0,
            anchor="nw",
            text="System Updates",
            fill="#000000",
            font=("Nunito SemiBold", 20 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_3.png"))
        image_3 = self.canvas_scroll.create_image(
            94.0,
            260.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_4.png"))
        image_4 = self.canvas_scroll.create_image(
            570.0,
            1081.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_5.png"))
        image_5 = self.canvas_scroll.create_image(
            570.0,
            847.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_6.png"))
        image_6 = self.canvas_scroll.create_image(
            915.0,
            675.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_7.png"))
        image_7 = self.canvas_scroll.create_image(
            94.0,
            764.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_8.png"))
        image_8 = self.canvas_scroll.create_image(
            94.0,
            597.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_9.png"))
        image_9 = self.canvas_scroll.create_image(
            570.0,
            511.0,
            image=image_image_9
        )

        image_image_10 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_10.png"))
        image_10 = self.canvas_scroll.create_image(
            94.0,
            428.0,
            image=image_image_10
        )

        image_image_11 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_11.png"))
        image_11 = self.canvas_scroll.create_image(
            570.0,
            342.0,
            image=image_image_11
        )

        self.canvas_scroll.create_text(
            150.0,
            851.0,
            width=680,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies",
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            809.0,
            anchor="nw",
            text="Realtime GPS",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )
        image_image_2 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_2.png"))
        image_2 = self.canvas_scroll.create_image(
            900.0,
            847.0,
            image=image_image_2
        )

        self.canvas_scroll.create_text(
            121.0,
            753.0,
            anchor="nw",
            text="GPS & Device Location",
            fill="#000000",
            font=("Nunito SemiBold", 20 * -1)
        )

        image_image_12 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_12.png"))
        image_12 = self.canvas_scroll.create_image(
            570.0,
            678.0,
            image=image_image_12
        )

        self.canvas_scroll.create_text(
            150.0,
            682.0,
            width=680,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            640.0,
            anchor="nw",
            text="Networking",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            121.0,
            586.0,
            anchor="nw",
            text="Dongle & Network",
            fill="#000000",
            font=("Nunito SemiBold", 20 * -1)
        )

        image_image_13 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_13.png"))
        image_13 = self.canvas_scroll.create_image(
            913.0,
            511.0,
            image=image_image_13
        )

        self.canvas_scroll.create_text(
            150.0,
            515.0,
            width=680,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu u",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            473.0,
            anchor="nw",
            text="System Language",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            121.0,
            417.0,
            anchor="nw",
            text="Languages",
            fill="#000000",
            font=("Nunito SemiBold", 20 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            346.0,
            width=680,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            304.0,
            anchor="nw",
            text="System Version",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        image_image_14 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_14.png"))
        image_14 = self.canvas_scroll.create_image(
            940.0,
            342.0,
            image=image_image_14
        )

        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        self.window.mainloop()

