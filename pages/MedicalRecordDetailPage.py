import customtkinter
from tkinter import *
from tkinter import font
from colors import *
from helpers import *
from PIL import Image, ImageTk

import json
from pprint import pprint


class MedicalRecordDetailPage(Canvas, BasePage):

    def __init__(self, window, clicked_data, previous_page):

        self.window = window
        self.clicked_data = clicked_data
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.previous_page = previous_page
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

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordDetailFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        inactive_button_3 = relative_to_assets("control/MedicalRecordDetailFrame/button_3.png")
        active_button_3 = relative_to_assets("control/MedicalRecordDetailFrame/active_button_3.png")

        inactive_button_4 = relative_to_assets(f"control/MedicalRecordDetailFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/MedicalRecordDetailFrame/{self.lang_code}/active_button_4.png")

        create_hover_button(self.window, 1008.0, 563.0, 52.0, 52.0,
                            "#000000", inactive_button_3, active_button_3,
                            lambda: print("button clicked"))

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,
                            lambda: goToPage(self.previous_page(self.window)))

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

        try :
            img_diagnose_path = relative_to_image_capture(f"{self.clicked_data['gambar_penyakit']}")
            img = Image.open(img_diagnose_path)
            img_array = np.array(img)

            # Panggil fungsi crop_with_padding
            cropped_img_array = crop_with_padding(img_array, 1, (559, 471))
            cropped_img_pil = Image.fromarray(cropped_img_array)
            cropped_img = ImageTk.PhotoImage(cropped_img_pil)

        except:
            cropped_img = PhotoImage(
                file=relative_to_assets("control/MedicalRecordDetailFrame/image_5.png"))

        # Tampilkan gambar di tkinter
        image_5 = self.create_image(
            790.0,
            388.0,
            image=cropped_img
        )

        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=380,
                                                         height=200,
                                                         fg_color="#FFFFFF",
                                                         scrollbar_button_hover_color="#404040",
                                                         scrollbar_fg_color="#FFFFFF",
                                                         bg_color="#FFFFFF",
                                                         border_width=0)

        self.my_frame.place(x=65, y=400)
        self.canvas_scroll = Canvas(self.my_frame,
                                    width=380,
                                    height=500,
                                    bg="#FFFFFF",
                                    highlightthickness=0,
                                    borderwidth=0)
        self.canvas_scroll.pack()

        self.update_cards()

    def update_cards(self):
        self.canvas_scroll.delete("all")
        schedule_images = []

        x_col1 = 72.0
        x_col2 = 245.0
        y_start = 421.0
        y_gap = 34.0

        self.create_text(
            x_col1,
            362.0,
            anchor="nw",
            text=self.clicked_data['nama_pasien'],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.canvas_scroll.create_text(
            x_col1,
            y_start,
            anchor="nw",
            text=f"NIK",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col2,  # Kolom 2
            y_start,  # Baris 1
            anchor="nw",
            text=": " + self.clicked_data['NIK'],
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col1,
            y_start + y_gap,
            anchor="nw",
            text=f"{self.data_localization['check_date'].title()}",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col2,  # Kolom 2
            y_start + y_gap,  # Baris 1
            anchor="nw",
            text=": "+self.clicked_data['tanggal_pemeriksaan'].strftime("%d %B %Y"),
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col1,  # Kolom 1
            y_start + 2 * y_gap,  # Baris 2
            anchor="nw",
            text=f"{self.data_localization['diagnosis_result']}",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        nama_penyakit = ": " + self.clicked_data['nama_penyakit']
        max_width = 250
        font_nama_penyakit = ("Nunito Bold", 19 * -1)

        nama_penyakit_id = self.canvas_scroll.create_text(
            x_col2,  # Kolom 2
            y_start + 2 * y_gap,  # Baris 2
            anchor="nw",
            text=nama_penyakit,
            fill="#1E5C2A",
            font=font_nama_penyakit,
            width=max_width
        )

        # Ambil bounding box dari teks yang baru dibuat
        bbox_penyakit = self.canvas_scroll.bbox(nama_penyakit_id)

        penyakit_height = bbox_penyakit[3] - bbox_penyakit[1]

        self.canvas_scroll.create_text(
            x_col1,  # Kolom 1
            y_start + (2 * y_gap) + penyakit_height + 10,
            anchor="nw",
            text=f"{self.data_localization['confidence_level']}",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col2,
            y_start + (2 * y_gap) + penyakit_height + 10,
            anchor="nw",
            text=f": {self.clicked_data['tingkat_keyakinan']}%",
            fill="#1E5C2A",
            font=("Nunito Bold", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col1,  # Kolom 1
            y_start + (3 * y_gap) + penyakit_height,
            anchor="nw",
            text=f"Alamat Pasien",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col2,
            y_start + (3 * y_gap) + penyakit_height,
            anchor="nw",
            text=f": Jalan ABCD no. 1234",
            fill="#404040",
            font=("Nunito Bold", 16 * -1)
        )

        self.canvas_scroll.create_text(
            x_col1,
            y_start + (4 * y_gap) + penyakit_height + 10,
            anchor="nw",
            text=self.clicked_data['deskripsi_penyakit'],
            fill="#404040",
            font=("Nunito Bold", 16 * -1),
            width=380,
            justify="left"
        )

        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))

        self.window.mainloop()
