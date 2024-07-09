import tkinter as tk
from tkinter import *
from colors import *
from helpers import *

from pages import DiagnosisPage
from pages import HomePage


class PatientQueuePage(Canvas, BasePage):
    def __init__(self, window):
        self.window = window
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data = None):
        self.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_1.png"))
        image_1 = self.create_image(
            382.0,
            405.0,
            image=image_image_1
        )

        self.create_text(
            86.0,
            219.5,
            anchor="nw",
            text="Alma Liakua Mutia",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            86.0,
            278.5,
            anchor="nw",
            text="Jenis Kelamin               : ",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            278.5,
            anchor="nw",
            text="Perempuan",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            312.5,
            anchor="nw",
            text="Tanggal Lahir              : ",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            312.5,
            anchor="nw",
            text="Selasa, 16 April 2024",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            346.5,
            anchor="nw",
            text="Alamat Domisili           : ",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            275.0,
            346.5,
            anchor="nw",
            text="Jl. Langko No. 72, Mataram, Ntb",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            86.0,
            380.5,
            anchor="nw",
            text="Diagnosa Terakhir       :",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            257.0,
            384.5,
            anchor="nw",
            text="OMA PERFORASI",
            fill="#1E5C2A",
            font=("Nunito Bold", 19 * -1)
        )
        
        text_widget = tk.Text(self.window, wrap="word", font=("Nunito regular", 12), bg="#FFFFFF", fg="#404040", bd=0, highlightthickness=0)
        text_widget.place(x=86, y=417.5, width=600, height=150)  # ukuran box

        # Mengisi teks ke Text Widget
        text_content = """OMA Perofrasi adalah gangguan ........ . Dicirikan dengan ....... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. """
        text_widget.insert(tk.END, text_content)

        text_widget.tag_configure("justify", justify="left")
        text_widget.tag_add("justify", "1.0", "end")

        # Menonaktifkan Text Widget agar tidak dapat diedit
        text_widget.configure(state="disabled")

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_2.png"))
        image_2 = self.create_image(
            897.0,
            339.0,
            image=image_image_2
        )

        self.create_rectangle(
            738.0,
            349.99997228697987,
            1056.0,
            351.0,
            fill="#E0E0E0",
            outline="")

        self.create_text(
            744.5,
            277.5,
            anchor="nw",
            text="Penyakit Telinga",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_3.png"))
        image_3 = self.create_image(
            754.5,
            313.0,
            image=image_image_3
        )

        self.create_text(
            774.5,
            301.5,
            anchor="nw",
            text="02 Januari 2024",
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_4.png"))
        image_4 = self.create_image(
            754.5,
            334.5,
            image=image_image_4
        )

        self.create_text(
            773.5,
            326.0,
            anchor="nw",
            text="RS. Provinsi Nusa Tenggara Barat",
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("control/PatientQueueFrame/button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=994.5,
            y=289.0,
            width=44.0,
            height=44.0
        )

        self.create_rectangle(
            738.0,
            430.49997228697987,
            1056.0,
            431.5,
            fill="#E0E0E0",
            outline="")

        self.create_text(
            744.5,
            358.0,
            anchor="nw",
            text="Penyakit Telinga",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_5.png"))
        image_5 = self.create_image(
            754.5,
            393.5,
            image=image_image_5
        )

        self.create_text(
            774.5,
            382.0,
            anchor="nw",
            text="02 Januari 2024",
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_6.png"))
        image_6 = self.create_image(
            754.5,
            415.0,
            image=image_image_6
        )

        self.create_text(
            773.5,
            406.5,
            anchor="nw",
            text="RS. Provinsi Nusa Tenggara Barat",
            fill="#404040",
            font=("Nunito Regular", 12 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=994.5,
            y=369.5,
            width=44.0,
            height=44.0
        )

        self.create_text(
            752.0,
            224.0,
            anchor="nw",
            text="Riwayat Pemeriksaan",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_7.png"))
        image_7 = self.create_image(
            897.0,
            592.0,
            image=image_image_7
        )

        self.create_text(
            752.0,
            520.0,
            anchor="nw",
            text="Asuransi Kesehatan",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            752.0,
            570.0,
            anchor="nw",
            text="No Asuransi     : ",
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            865.0,
            570.0,
            anchor="nw",
            text="000863002321023",
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            594.0,
            anchor="nw",
            text="Jenis Asuransi  : ",
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            864.0,
            594.0,
            anchor="nw",
            text="BPJS",
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            618.0,
            anchor="nw",
            text="Kelas Asuransi : ",
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            864.0,
            618.0,
            anchor="nw",
            text="Kelas 1",
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        self.create_text(
            752.0,
            642.0,
            anchor="nw",
            text="Fasilitas Kesehatan : ",
            fill="#404040",
            font=("Nunito Regular", 13 * -1)
        )

        self.create_text(
            891.0,
            642.0,
            anchor="nw",
            text="Puskesmas Selaparang",
            fill="#404040",
            font=("Nunito Bold", 13 * -1)
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_8.png"))
        image_8 = self.create_image(
            566.0,
            89.0,
            image=image_image_8
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text="RS. Universitas Mataram",
            fill="#FFFFFF",
            font=("Nunito Black", 14 * -1)
        )

        self.create_text(
            130.0,
            144.5,
            anchor="nw",
            text="Unit THT",
            fill="#F1F1F1",
            font=("Nunito SemiBold", 12 * -1)
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_9.png"))
        image_9 = self.create_image(
            89.0,
            139.0,
            image=image_image_9
        )

        image_image_10 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_10.png"))
        image_10 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_10
        )

        image_image_11 = PhotoImage(
            file=relative_to_assets("control/PatientQueueFrame/image_11.png"))
        image_11 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_11
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        inactive_button_3 = relative_to_assets("control/PatientQueueFrame/button_3.png")
        active_button_3 = relative_to_assets("control/PatientQueueFrame/active_button_3.png")
        
        inactive_button_4 = relative_to_assets("control/PatientQueueFrame/button_4.png")
        active_button_4 = relative_to_assets("control/PatientQueueFrame/active_button_4.png")
        
        inactive_button_5 = relative_to_assets("control/PatientQueueFrame/button_5.png")
        active_button_5 = relative_to_assets("control/PatientQueueFrame/active_button_5.png")

        create_hover_button(self.window, 59.5, 633.5, 192.0, 54.0, 
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: goToPage(HomePage.HomePage(self.window)))
        
        create_hover_button(self.window, 284.5, 633.5, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: goToPage(DiagnosisPage.DiagnosisPage(self.window)))
        
        create_hover_button(self.window, 509.5, 633.5, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_5, active_button_5,  
                            lambda: print("button_5 clicked"))

        self.window.mainloop()