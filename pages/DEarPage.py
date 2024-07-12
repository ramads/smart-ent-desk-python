from tkinter import *
from colors import *
from helpers import *
from pages import DEarProcessPage, DiagnosisPage
from notificationBar import notificationBar

class DEarPage(Canvas, BasePage):

    def __init__(self, window, temp_data=None, diagnosis_type=None):
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
        self.temp_data = temp_data
        self.temp_data['diagnosis_type'] = diagnosis_type

    def drawPage(self):
        self.place(x=0, y=0)

        wifi_clock_app = notificationBar(self.window)

        inactive_button_1 = relative_to_assets("control/DEarFrame/button_1.png")
        active_button_1 = relative_to_assets("control/DEarFrame/active_button_1.png")
        
        inactive_button_2 = relative_to_assets("control/DEarFrame/button_2.png")
        active_button_2 = relative_to_assets("control/DEarFrame/active_button_2.png")

        create_hover_button(self.window, 431.0, 600.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DiagnosisPage.DiagnosisPage(self.window, self.temp_data['id_patient'])))
        
        create_hover_button(self.window, 575.0, 600.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: goToPage(DEarProcessPage.DEarProcessPage(self.window, self.temp_data)))
        

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/DEarFrame/image_2.png"))
        image_2 = self.create_image(
            571.0,
            414.0,
            image=image_image_2
        )

        self.create_text(
            560.0,
            565.0,
            anchor="center",
            text="Sebelum mengambil gambar silakan ambil Otoscope dan pastikan sudah diarahkan dengan benar.",
            fill="#8A8C8F",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            565.0,
            522.0,
            anchor="center",
            text="Diagnosa Telinga",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarFrame/image_3.png"))
        image_3 = self.create_image(
            568.0,
            326.0,
            image=image_image_3
        )

        self.window.mainloop()