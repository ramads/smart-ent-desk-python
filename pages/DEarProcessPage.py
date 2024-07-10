import os

import cv2
from tkinter import *
from colors import *
from helpers import *
from config import CAMERA_INDEX
from PIL import Image, ImageTk
from pages import DEarPage, PreviewImagePage
from libs.serial_com import SerialCom


class DEarProcessPage(Canvas, BasePage):
    capture_image = None
    after_cam_id = 0
    image_dir = "./" + DIR_TEMP_IMAGE
    text_command = ""

    def __init__(self, window, id_patient=None, organ=None):
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.id_patient = id_patient
        self.organ = organ
        os.makedirs(self.image_dir, exist_ok=True)
        self.window = window
        self.vidCap = cv2.VideoCapture(CAMERA_INDEX)
        self.ret, self.frame = self.vidCap.read()
        if not self.ret:
            print("Failed to grab frame")
        
    
        

    def updateCameraFrame(self):
        self.ret, self.frame = self.vidCap.read()

        if self.ret:
            self.frame = cv2.resize(self.frame, (604, 538))
            opencv_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(opencv_image))
            self.create_image(354.0, 339.0, image=self.captured_image)

        self.after_cam_id = self.after(10, self.updateCameraFrame)

    def onCapture(self, image_name):
        if self.frame is not None:
            filename = os.path.join(self.image_dir, f"{image_name}.jpg")
            saved_img = cv2.resize(self.frame, (1019, 452))
            cv2.imwrite(filename, saved_img)

            print(f"Image captured and saved as '{filename}'")
            self.onStopCamera()

            goToPage(PreviewImagePage.PreviewImagePage(self.window, self.id_patient, self.organ))

    def onStopCamera(self):
        self.vidCap.release()
        cv2.destroyAllWindows()
        self.after_cancel(self.after_cam_id)

    def backToPrevPage(self):
        self.onStopCamera()
        goToPage(DEarPage.DEarPage(self.window))

    def sendSerialCommand(self, command):
        if command == 4: command = 0
        elif command > 4: command = command - 1

        self.text_command = f"Send serial command: {command}"
        self.itemconfig(self.commandText, text=self.text_command)
        # print(self.text_command)

    def drawDemoSerialCommand(self):
        self.commandText = self.create_text(
            726.0,
            675.0,
            anchor="nw",
            text=self.text_command,
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

    def drawPage(self):
        self.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_1.png"))
        image_1 = self.create_image(
            354.0,
            378.0,
            image=image_image_1
        )

        inactive_button_1 = relative_to_assets("control/DEarProcessFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DEarProcessFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/DEarProcessFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DEarProcessFrame/active_button_2.png")

        create_hover_button(self.window, 158.0, 632.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: self.backToPrevPage())
        
        create_hover_button(self.window, 358.0, 632.0, 192.0, 54.0,
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: self.onCapture("test_image"))
        
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
            text="Kontrol Alat",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            375.0,
            anchor="nw",
            text="Tekanan Air (Spray)",
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

        self.create_text(
            726.0,
            531.0,
            anchor="nw",
            text="Tekanan Pompa Penghisap",
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
            text="Informasi Pasien",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            726.0,
            126.0,
            anchor="nw",
            text="Alma Liakua Mutia",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            726.0,
            160.0,
            anchor="nw",
            text="No Asuransi     : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
            160.0,
            anchor="nw",
            text="000863002321023",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            184.0,
            anchor="nw",
            text="Jenis Asuransi  : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
            184.0,
            anchor="nw",
            text="BPJS",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            208.0,
            anchor="nw",
            text="Kelas Asuransi : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            850.0,
            208.0,
            anchor="nw",
            text="Kelas 1",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        self.create_text(
            726.0,
            232.0,
            anchor="nw",
            text="Fasilitas Kesehatan : ",
            fill="#404040",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            885.0,
            232.0,
            anchor="nw",
            text="Puskesmas Selaparang",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_5.png"))
        image_5 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/DEarProcessFrame/image_6.png"))
        image_6 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_6
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.drawDemoSerialCommand()

        switch_button_image(0)
        self.after(10, self.updateCameraFrame)
        self.window.mainloop()