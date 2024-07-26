import customtkinter
from tkinter import *
from tkinter import ttk
from colors import *
from helpers import *
# from notificationBar import notificationBar


from pages import HomePage

from database.models.Diagnosis import DiagnosisModel
import json


class Settings(Canvas, BasePage):

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

        self.drawPage()

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def change_language(self, language):
        if language == "Indonesia" or language == "Indonesian":
            lang_code = "id"
        else:
            lang_code = "en"

        with open("config.json", "r") as file:
            data = json.load(file)
            data["language"] = lang_code
        
        with open("config.json", "w") as file:
            json.dump(data, file)

        self.lang_code = lang_code
        self.data_localization = self.get_localization()
        self.drawPage()


    def show(self, label):
        print(label)
        # self.temp_data['result_1'] = (label, self.temp_data['result_1'][1])
        # self.temp_data['is_corrected'] = False
        # self.temp_data['correction_reason'] = entry_1.get("1.0", "end-1c")
        # goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data))

    def create_option_menu(self, parent, options, geometry, action=None):
        clicked = StringVar()
        clicked.set("Pilih Label")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Rounded.TMenubutton",
                        relief="flat",
                        padding=2,
                        background="#FFFFFF",
                        foreground="black",
                        borderwidth=1,
                        bordercolor="black",
                        border=8,
                        focusthickness=3,
                        focuscolor="#FFFFFF",
                        anchor="w")
        style.map("Rounded.TMenubutton",
                  background=[("active", "skyblue")])

        drop = ttk.OptionMenu(parent, clicked, options[0], *options, command=lambda x: action(clicked.get()))
        drop.config(style="Rounded.TMenubutton")
        drop.pack(pady=0)

        x, y, width, height = geometry
        drop.place(x=x, y=y, width=width, height=height)

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

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
            text=self.data_localization['settings'],
            fill="#000000",
            font=("Nunito SemiBold", 25 * -1)
        )

        inactive_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/MedicalRecordFrame/{self.lang_code}/active_button_4.png")

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
        self.canvas_scroll = Canvas(self.my_frame,
                                    width=955,
                                    height=1030,
                                    bg="#FFFFFF",
                                    highlightthickness=0,
                                    borderwidth=0)
        self.canvas_scroll.pack()


        self.update_cards()



    def update_cards(self):
        self.canvas_scroll.delete("all")

        button_images = []

        # for i in range(len(self.history_data)):
        #     y_offset = i * 50


        # Define options and geometries
        if self.lang_code == "id":
            options_1 = ['Indonesia', 'Inggris']
        else:
            options_1 = ['English', 'Indonesian']
        options_2 = ["v.1.1", "v.1.2"]
        options_3 = ["v.1.1", "v.1.2"]

        self.create_option_menu(self.canvas_scroll, options_1, (760, 255, 155, 27), self.change_language)
        self.create_option_menu(self.canvas_scroll, options_2, (810, 86, 105, 27), self.show)
        self.create_option_menu(self.canvas_scroll, options_3, (760, 590, 155, 27), self.show)


        self.canvas_scroll.create_text(
            121.0,
            249.0,
            anchor="nw",
            text=self.data_localization["system_update_title"],
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
            text=self.data_localization["realtime_gps_description"],
            fill="#404040",
            font=("Nunito regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            809.0,
            anchor="nw",
            text=self.data_localization["realtime_gps_title"],
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )
        image_image_2 = PhotoImage(
            file=relative_to_assets(f"control/SettingsFrame/image_2.png"))
        image_2 = self.canvas_scroll.create_image(
            913.0,
            847.0,
            image=image_image_2
        )

        self.canvas_scroll.create_text(
            121.0,
            753.0,
            anchor="nw",
            text=self.data_localization["realtime_gps_subtitle"],
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
            text=self.data_localization["dongle_network_description"],
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            640.0,
            anchor="nw",
            text=self.data_localization["dongle_network_subtitle"],
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            121.0,
            586.0,
            anchor="nw",
            text=self.data_localization["dongle_network_title"],
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
            text=self.data_localization["system_language_description"],
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            473.0,
            anchor="nw",
            text=self.data_localization["system_language_subtitle"],
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.canvas_scroll.create_text(
            121.0,
            417.0,
            anchor="nw",
            text=self.data_localization["system_language_title"],
            fill="#000000",
            font=("Nunito SemiBold", 20 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            346.0,
            width=680,
            anchor="nw",
            text=self.data_localization["system_update_description"],
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.canvas_scroll.create_text(
            150.0,
            304.0,
            anchor="nw",
            text=self.data_localization["system_update_subtitle"],
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

