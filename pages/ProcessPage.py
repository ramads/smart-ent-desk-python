import os

from tkinter import *

import config
from colors import *
from helpers import *
from PIL import Image, ImageTk
from pages import DiagnosisStartPage, PreviewImagePage, CameraDisconnectedPage
from libs.serial_com import SerialCom

from database.models import Patient, MedicalRecord

import json
from pprint import pprint

class ProcessPage(Canvas, BasePage):
    capture_image = None
    seriCom = SerialCom()
    after_cam_id = 0
    image_dir = "./" + DIR_TEMP_IMAGE
    text_command = ""
    countdown_seconds = 0

    def __init__(self, window, temp_data=None):
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
        pprint(temp_data)
        self.patient = Patient.PatientModel()
        self.medical_record = MedicalRecord.MedicalRecordModel()
        self.get_patient_data()
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.seriCom.connect()
        os.makedirs(self.image_dir, exist_ok=True)
        self.window = window
        self.vidCap = None
        self.zoom_factor = 1
        self.save_image = None
        self.camera_thread = None
        self.camera_open_thread = None
        self.timer = 0
        self.cam_index = config.CAMERA_PORT
        self.countdown_seconds = 0
        self.buttons = []

        # Taruhin pop up reload camera

        # self.check_camera = False
        # while (self.check_camera is False):
        self.open_camera_in_thread()
        self.startCameraThread()

    def open_camera_in_thread(self):
        camera_open_thread = threading.Thread(target=self.try_open_camera)
        camera_open_thread.start()

        camera_open_thread.join()

    def try_open_camera(self):
        vidCap = cv2.VideoCapture(self.cam_index)
        if vidCap.isOpened():
            ret, frame = vidCap.read()
            if ret:
                if self.vidCap is None:
                    self.vidCap = vidCap
                    self.frame = frame
                    print("----------->masuk")
                else:
                    vidCap.release()
                    print("masuk ga----------")
                self.check_camera = True
        else:
            print(f"Failed to open camera at index {self.cam_index}")

    def set_timer (self, second):
        if self.timer == second:
            self.timer = 0
        else:
            self.timer = second
        self.update_button_states()

    def update_button_states(self):
        for button, sec in self.buttons:
            if self.timer == sec:
                button.config(image=button.active_image)
                button.image = button.active_image  # Simpan referensi gambar aktif
            else:
                button.config(image=button.inactive_image)
                button.image = button.inactive_image  # Simpan referensi gambar inaktif

    def create_button(self, x, y, width, height, bg_color, inactive_image_path, active_image_path, sec):
        inactive_image = PhotoImage(file=relative_to_assets(inactive_image_path))
        active_image = PhotoImage(file=relative_to_assets(active_image_path))

        button = Button(
            self,
            image=inactive_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_timer(sec),
            relief="flat",
            activebackground=bg_color,
            bg=bg_color
        )

        button.place(x=x, y=y, width=width, height=height)

        # Simpan referensi gambar
        button.image = inactive_image
        button.active_image = active_image
        button.inactive_image = inactive_image

        # Simpan referensi tombol dan waktunya dalam list
        self.buttons.append((button, sec))

    def countdown(self, seconds):
        self.countdown_seconds = seconds
        self.window.after(1000, self.updateCountdown)

    def updateCountdown(self):
        if self.countdown_seconds > 0:
            self.countdown_seconds -= 1
            self.window.after(1000, self.updateCountdown)
        else:
            self.onCapture("test_image")

    def startCameraThread(self):
        self.camera_thread = threading.Thread(target=self.updateCameraFrame)
        self.camera_thread.start()

    def updateCameraFrame(self):
        if self.vidCap is None or not self.vidCap.isOpened():
            self.handle_camera_disconnection()
            return

        self.ret, self.frame = self.vidCap.read()

        if not self.ret:
            self.handle_camera_disconnection()
            return

        if self.ret:
            # self.frame = cv2.resize(self.frame, (604, 538))

            self.save_image = crop_and_save(self.frame, self.zoom_factor, (550, 550))

            opencv_PIL = crop_and_save(self.frame, self.zoom_factor, (604, 538))
            opencv_to_PIL = cv2.cvtColor(opencv_PIL, cv2.COLOR_BGR2RGBA)
            # opencv_to_PIL = cv2.cvtColor(self.save_image, cv2.COLOR_BGR2RGBA)
            self.capture_image = ImageTk.PhotoImage(image=Image.fromarray(opencv_to_PIL))
            self.create_image(354.0, 339.0, image=self.capture_image)


        if self.countdown_seconds > 0:
            self.create_text(
                575.0,
                525.0,
                anchor='nw',
                text=str(self.countdown_seconds),
                fill="#FFFFFF",
                font=("Nunito Bold", 60 * -1)
            )

        else:
            self.create_text(
                575.0,
                525.0,
                anchor='nw',
                text=str(self.timer),
                fill="#FFFFFF",
                font=("Nunito Bold", 60 * -1)
            )

        self.after_cam_id = self.after(20, self.updateCameraFrame)

    def handle_camera_disconnection(self):
        print("Camera disconnected or not functioning. Redirecting to CameraDisconnectedPage.")
        self.onStopCamera()
        self.window.after(0, lambda: goToPage(CameraDisconnectedPage.CameraDisconnectedPage(self.window, self.temp_data)))

    def onCapture(self, image_name):
        if self.frame is not None:
            filename = os.path.join(self.image_dir, f"{image_name}.jpg")
            # cv2.imwrite(filename, self.frame)

            # self.captured_image = np.array(self.captured_image)

            # saved_img = crop_and_save(self.frame, 1.2, (512, 512))
            cv2.imwrite(filename, self.save_image)



            print(f"Image captured and saved as '{filename}'")
            self.onStopCamera()

            goToPage(PreviewImagePage.PreviewImagePage(self.window, self.temp_data))

    def onStopCamera(self):
        if self.camera_thread is not None and self.camera_thread != threading.current_thread():
            self.camera_thread.join()
        if self.vidCap is not None:
            self.vidCap.release()
        cv2.destroyAllWindows()
        if self.after_cam_id != 0:
            self.after_cancel(self.after_cam_id)


    def get_patient_data(self):
        self.patient_data = self.patient.get_patient(self.temp_data['NIK'])
        self.medical_record_data = self.medical_record.get_medical_record_join_disease(self.temp_data['NIK'])


        pprint(self.patient_data)

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def backToPrevPage(self):
        self.onStopCamera()
        goToPage(DiagnosisStartPage.DiagnosisStartPage(self.window, self.temp_data))

    def sendSerialCommand(self, command):
        if command == 4:
            command = 0
        elif command > 4:
            command = command - 1

        # self.text_command = f"Send serial command: {command}"
        self.itemconfig(self.commandText, text=self.text_command)

        command = str(command)
        if command == "0":
            command = "o"
        self.seriCom.write_serial(command)

    def drawDemoSerialCommand(self):
        self.commandText = self.create_text(
            726.0,
            675.0,
            anchor="nw",
            text=self.text_command,
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

    def zoom_in(self):
        self.zoom_factor *= 1.1
        # self.update_image()

    def zoom_out(self):
        self.zoom_factor /= 1.1
        # self.update_image()

    def moving_image(self, direction):
        if direction=="up":
            pass


    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_1.png"))
        image_1 = self.create_image(
            354.0,
            378.0,
            image=image_image_1
        )

        inactive_button_1 = relative_to_assets(f"control/DEarProcessFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/DEarProcessFrame/{self.lang_code}/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/DEarProcessFrame/{self.lang_code}/button_2.png")
        active_button_2 = relative_to_assets(f"control/DEarProcessFrame/{self.lang_code}/active_button_2.png")

        inactive_button_3 = relative_to_assets(f"control/DEarProcessFrame/inactive_3s.png")
        active_button_3 = relative_to_assets(f"control/DEarProcessFrame/active_3s.png")

        inactive_button_4 = relative_to_assets(f"control/DEarProcessFrame/inactive_5s.png")
        active_button_4 = relative_to_assets(f"control/DEarProcessFrame/active_5s.png")

        inactive_button_5 = relative_to_assets(f"control/DEarProcessFrame/inactive_10s.png")
        active_button_5 = relative_to_assets(f"control/DEarProcessFrame/active_10s.png")

        left_arrow_hover = relative_to_assets(f"control/DEarProcessFrame/left_arrow_hover.png")
        left_arrow = relative_to_assets(f"control/DEarProcessFrame/left_arrow.png")

        right_arrow_hover = relative_to_assets(f"control/DEarProcessFrame/right_arrow_hover.png")
        right_arrow = relative_to_assets(f"control/DEarProcessFrame/right_arrow.png")

        up_arrow_hover = relative_to_assets(f"control/DEarProcessFrame/up_arrow_hover.png")
        up_arrow = relative_to_assets(f"control/DEarProcessFrame/up_arrow.png")

        bottom_arrow_hover = relative_to_assets(f"control/DEarProcessFrame/bottom_arrow_hover.png")
        bottom_arrow = relative_to_assets(f"control/DEarProcessFrame/bottom_arrow.png")

        create_hover_button(self.window, 50.0, 632.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: self.backToPrevPage())
        
        create_hover_button(self.window, 250.0, 632.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: self.countdown(self.timer))

        create_hover_button(self.window, 325.0, 85.0, 69.0, 69.0,
                            "#000000", up_arrow, up_arrow_hover,
                            lambda: print("berhasil"))

        create_hover_button(self.window, 325.0, 520.0, 69.0, 69.0,
                            "#000000", bottom_arrow, bottom_arrow_hover,
                            lambda: print("berhasil"))

        create_hover_button(self.window, 65.0, 300.0, 69.0, 69.0,
                            "#000000", left_arrow, left_arrow_hover,
                            lambda: print("berhasil"))

        create_hover_button(self.window, 575.0, 300.0, 69.0, 69.0,
                            "#000000", right_arrow, right_arrow_hover,
                            lambda: self.backToPrevPage())

        self.create_button(450.0, 632.0, 62.0, 54.0, "#FFFFFF", inactive_button_3, active_button_3, 3)
        self.create_button(520.0, 632.0, 62.0, 54.0, "#FFFFFF", inactive_button_4, active_button_4, 5)
        self.create_button(590.0, 632.0, 62.0, 54.0, "#FFFFFF", inactive_button_5, active_button_5, 10)

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_3.png"))
        image_3 = self.create_image(
            901.0,
            500.0,
            image=image_image_3
        )

        self.create_text(
            726.0,
            319.0,
            anchor="nw",
            text=self.data_localization['tool_control'].title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            375.0,
            anchor="nw",
            text=self.data_localization['water_pressure'].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        # Load images
        active_button_image_3 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_3.png"))
        button_image_3 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_3.png"))

        active_button_image_4 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_4.png"))
        button_image_4 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_4.png"))

        active_button_image_5 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_5.png"))
        button_image_5 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_5.png"))

        active_button_image_6 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_6.png"))
        button_image_6 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_6.png"))

        active_button_image_7 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_7.png"))
        button_image_7 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_7.png"))

        active_button_image_8 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_8.png"))
        button_image_8 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_8.png"))

        active_button_image_9 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_9.png"))
        button_image_9 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_9.png"))

        active_button_image_10 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/active_button_10.png"))
        button_image_10 = PhotoImage(file=relative_to_assets("control/DEarProcessFrame/button_10.png"))

        buttons = []

        # Fungsi untuk mengganti gambar tombol
        def switch_button_image(button_index):
            for index, button in enumerate(buttons):
                if index == button_index:
                    button.config(image=button.active_image)
                else:
                    button.config(image=button.image)

            self.sendSerialCommand(button_index)
            # Logika tambahan untuk mengaktifkan tombol terkait
            if button_index in [0, 1, 2, 3]:  # Jika tombol 3, 4, 5, atau 6 diklik
                buttons[4].config(image=buttons[4].active_image)  # Aktifkan tombol 7
            elif button_index in [4, 5, 6, 7]:  # Jika tombol 7, 8, 9, atau 10 diklik
                buttons[0].config(image=buttons[0].active_image)  # Aktifkan tombol 3

        # Membuat tombol dan menambahkannya ke list buttons
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(0),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_3.place(
            x=720.3446052083908,
            y=425.4611282348633,
            width=79.07769703770293,
            height=79.07769703770293
        )
        button_3.image = button_image_3
        button_3.active_image = active_button_image_3
        buttons.append(button_3)

        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(1),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_4.place(
            x=814.4223022460938,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_4.image = button_image_4
        button_4.active_image = active_button_image_4
        buttons.append(button_4)

        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(2),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_5.place(
            x=908.5,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_5.image = button_image_5
        button_5.active_image = active_button_image_5
        buttons.append(button_5)

        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(3),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_6.place(
            x=1002.57763671875,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_6.image = button_image_6
        button_6.active_image = active_button_image_6
        buttons.append(button_6)

        # Membuat tombol dan menambahkannya ke list buttons
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(4),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_7.place(
            x=720.3446052083908,
            y=581.4611282348633,
            width=79.07769703770293,
            height=79.07769703770305
        )
        button_7.image = button_image_7
        button_7.active_image = active_button_image_7
        buttons.append(button_7)

        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(5),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_8.place(
            x=814.4223022460938,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_8.image = button_image_8
        button_8.active_image = active_button_image_8
        buttons.append(button_8)

        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(6),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_9.place(
            x=908.5,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_9.image = button_image_9
        button_9.active_image = active_button_image_9
        buttons.append(button_9)

        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_button_image(7),
            relief="flat",
            activebackground="#FFFFFF",
            bg="#FFFFFF"
        )
        button_10.place(
            x=1002.57763671875,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )
        button_10.image = button_image_10
        button_10.active_image = active_button_image_10
        buttons.append(button_10)

        # zoom in and zoom out button
        inactive_button_2 = relative_to_assets(f"control/DEarProcessFrame/zoom_in.png")
        active_button_2 = relative_to_assets(f"control/DEarProcessFrame/zoom_in_inactive.png")

        inactive_button_3 = relative_to_assets(f"control/DEarProcessFrame/zoom_out.png")
        active_button_3 = relative_to_assets(f"control/DEarProcessFrame/zoom_out_inactive.png")

        create_hover_button(self.window, 75.5, 475.0, 52.0, 52.0,
                            "#000000", inactive_button_2, active_button_2,
                            lambda: self.zoom_in())

        create_hover_button(self.window, 75.5, 535.0, 52.0, 52.0,
                            "#000000", inactive_button_3, active_button_3,
                            lambda: self.zoom_out())

        self.create_text(
            726.0,
            531.0,
            anchor="nw",
            text=self.data_localization['pump_pressure'].title(),
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_4.png"))
        image_4 = self.create_image(
            901.0,
            161.0,
            image=image_image_4
        )

        self.create_text(
            726.0,
            76.0,
            anchor="nw",
            text=self.data_localization['information_patient'].title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            126.0,
            anchor="nw",
            text=self.patient_data['nama_pasien'],
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            726.0,
            160.0,
            anchor="nw",
            text=f"{self.data_localization['gender_type'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            885.0,
            160.0,
            anchor="nw",
            text=self.patient_data['jenis_kelamin'].capitalize(),
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            184.0,
            anchor="nw",
            text=f"{self.data_localization['latest_diagnose'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            885.0,
            184.0,
            anchor="nw",
            text=self.medical_record_data[0]['nama_penyakit'].capitalize(),
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            208.0,
            anchor="nw",
            text=f"{self.data_localization['patient_address'].capitalize()} :",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            885.0,
            208.0,
            anchor="nw",
            text=self.patient_data['alamat'].title(),
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.drawDemoSerialCommand()

        switch_button_image(0)
        # self.after(10, self.updateCameraFrame)
        self.window.mainloop()