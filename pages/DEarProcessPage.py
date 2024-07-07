import cv2
from tkinter import *
from colours import *
from helpers import *
from PIL import Image, ImageTk
# from pages.DEarPage import DEarPage


class DEarProcessPage(Canvas, BasePage):
    capture_image = None

    def __init__(self, window):
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.window = window
        self.vidCap = cv2.VideoCapture(0)
        self.ret, self.frame = self.vidCap.read()
        if not self.ret:
            print("Failed to grab frame")

        print("inisialisasi!")

    def updateCameraFrame(self):
        print("update frame!")
        self.ret, self.frame = self.vidCap.read()

        if self.ret:
            self.frame = cv2.resize(self.frame, (604, 538))
            opencv_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(opencv_image))
            self.create_image(354.0, 339.0, image=self.captured_image)

        self.after(10, self.updateCameraFrame)

    def onCapture(self):
        if self.frame is not None:
            # cv2.imwrite(filename, frame)
            print(f"Image captured and saved'")

    def onStopCamera(self):
        self.vidCap.release()
        cv2.destroyAllWindows()
        # goToPage(DEarPage(self.window))

    def drawPage(self):
        self.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/frame3/image_1.png"))
        image_1 = self.create_image(
            354.0,
            378.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("control/frame3/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=158.0,
            y=632.0,
            width=192.0,
            height=54.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/frame3/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=358.0,
            y=632.0,
            width=192.0,
            height=54.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/frame3/image_3.png"))
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

        button_image_3 = PhotoImage(
            file=relative_to_assets("control/frame3/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=720.3446052083908,
            y=425.4611282348633,
            width=79.07769703770293,
            height=79.07769703770293
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("control/frame3/button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=814.4223022460938,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("control/frame3/button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=908.5,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("control/frame3/button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=1002.57763671875,
            y=425.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        self.create_text(
            726.0,
            531.0,
            anchor="nw",
            text="Tekanan Pompa Penghisap",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("control/frame3/button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=720.3446052083908,
            y=581.4611282348633,
            width=79.07769703770293,
            height=79.07769703770305
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("control/frame3/button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=814.4223022460938,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("control/frame3/button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=908.5,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("control/frame3/button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        button_10.place(
            x=1002.57763671875,
            y=581.461181640625,
            width=79.07769012451172,
            height=79.07769012451172
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/frame3/image_4.png"))
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
            839.0,
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
            838.0,
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
            838.0,
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
            865.0,
            232.0,
            anchor="nw",
            text="Puskesmas Selaparang",
            fill="#404040",
            font=("Nunito Bold", 15 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/frame3/image_5.png"))
        image_5 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/frame3/image_6.png"))
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

        self.after(10, self.updateCameraFrame)
        self.window.mainloop()