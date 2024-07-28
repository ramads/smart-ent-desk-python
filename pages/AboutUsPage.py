import customtkinter
from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage
from pages import MedicalRecordDetailPage
from pages import MedicalRecordEditPage

from database.models.Hospital import HospitalModel
from config import DUMMY_HOSPITAL

import json


class AboutUsPage(Canvas, BasePage):

    def __init__(self, window):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.data_hospital = HospitalModel().get_hospital(DUMMY_HOSPITAL)

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
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)


        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=1025,
                                                         height=500,
                                                         fg_color=BACKGROUND_COLOUR,
                                                         scrollbar_button_hover_color="#404040",
                                                         scrollbar_fg_color=BACKGROUND_COLOUR,
                                                         bg_color=BACKGROUND_COLOUR,
                                                         border_width=0)

        self.my_frame.place(x=40, y=140)
        self.canvas_scroll = Canvas(self.my_frame,
                                    width=1025,
                                    height=1100,
                                    bg=BACKGROUND_COLOUR,
                                    highlightthickness=0,
                                    borderwidth=0)
        self.canvas_scroll.pack()

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_6.png"))
        image_6 = self.create_image(
            566.0,
            89.0,
            image=self.image_image_6
        )

        inactive_back = relative_to_assets(f"control/AboutUsFrame/{self.lang_code}/back.png")
        active_back = relative_to_assets(f"control/AboutUsFrame/{self.lang_code}/active_back.png")

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_back, active_back,
                            lambda: goToPage(HomePage.HomePage(self.window)))

        self.update_cards()

    def update_cards(self):
        self.canvas_scroll.delete("all")

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_2.png"))
        image_2 = self.canvas_scroll.create_image(
            560.0,
            332.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_3.png"))
        image_3 = self.canvas_scroll.create_image(
            840.0,
            973.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_4.png"))
        image_4 = self.canvas_scroll.create_image(
            322.0,
            973.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_5.png"))
        image_5 = self.canvas_scroll.create_image(
            213.0,
            644.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_6.png"))
        image_6 = self.canvas_scroll.create_image(
            560.0,
            644.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_7.png"))
        image_7 = self.canvas_scroll.create_image(
            907.0,
            644.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_8.png"))
        image_8 = self.canvas_scroll.create_image(
            837.0,
            361.0361328125,
            image=self.image_image_8
        )

        self.canvas_scroll.create_text(
            78.0,
            248.0,
            anchor="nw",
            width=520,
            text=self.data_hospital['tentang_rumah_sakit'],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            78.0,
            186.0,
            anchor="nw",
            text=self.data_localization["about_us"].title(),
            fill="#404040",
            font=("Nunito Bold", 28 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            595.5,
            anchor="nw",
            text=self.data_hospital['jumlah_partner'],
            fill="#85C13D",
            font=("Nunito Bold", 92 * -1)
        )

        self.canvas_scroll.create_text(
            110.0,
            572.0,
            anchor="nw",
            text=self.data_localization["hospital_partner"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            550.0,
            698.0,
            anchor="nw",
            text=self.data_hospital['jumlah_award'],
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_9.png"))
        image_9 = self.canvas_scroll.create_image(
            560.5,
            643.5,
            image=self.image_image_9
        )

        self.canvas_scroll.create_text(
            500.0,
            572.0,
            anchor="nw",
            text=self.data_localization["award"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            830.0,
            595.5,
            anchor="nw",
            text=self.data_hospital['jumlah_tenang_ahli'],
            fill="#85C13D",
            font=("Nunito Bold", 92 * -1)
        )

        self.canvas_scroll.create_text(
            850.0,
            572.0,
            anchor="nw",
            text=self.data_localization["experts"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_10.png"))
        image_10 = self.canvas_scroll.create_image(
            322.0,
            973.5,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_11.png"))
        image_11 = self.canvas_scroll.create_image(
            654.0,
            1122.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_12.png"))
        image_12 = self.canvas_scroll.create_image(
            654.0,
            1051.0,
            image=self.image_image_12
        )

        self.canvas_scroll.create_text(
            694.0,
            985.0,
            anchor="nw",
            text=self.data_hospital['email_rumah_sakit'],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_13.png"))
        image_13 = self.canvas_scroll.create_image(
            654.0,
            980.0,
            image=self.image_image_13
        )

        self.canvas_scroll.create_text(
            694.0,
            895.0,
            anchor="nw",
            width=350,
            text=self.data_hospital['alamat_rumah_sakit'],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("control/AboutUsFrame/image_14.png"))
        image_14 = self.canvas_scroll.create_image(
            654.0,
            890.0,
            image=self.image_image_14
        )

        self.canvas_scroll.create_text(
            637.0,
            804.5,
            anchor="nw",
            text=self.data_localization["contact"].title(),
            fill="#404040",
            font=("Nunito Bold", 28 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            1127.0,
            anchor="nw",
            text=self.data_hospital['situs_rumah_sakit'],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            1095.5,
            anchor="nw",
            text=self.data_localization["website"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            1056.0,
            anchor="nw",
            text=self.data_hospital['phone_number_rumah_sakit'],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            1024.5,
            anchor="nw",
            text=self.data_localization["telephone"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            953.5,
            anchor="nw",
            text=self.data_localization["email"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            694.0,
            863.5,
            anchor="nw",
            text=self.data_localization["office_address"].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        # self.window.mainloop()

