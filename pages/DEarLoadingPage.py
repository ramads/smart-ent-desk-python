import threading
from tkinter import *
from tkinter import ttk
from colors import *
from helpers import *

from pages import DEarResultPage
from machine_learning.image_predictor import ImagePredictor


class DEarLoadingPage(Canvas, BasePage):
    result_1 = ("",0)
    result_2 = ("",0)
    result_3 = ("",0)

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
        self.drawPage()
    def run_prediction(self):
        predictor = ImagePredictor()
        image_path = 'temp_image/test_image.jpg'

        self.result_1, self.result_2, self.result_3 = predictor.predict(image_path)

    def start(self):
        self.p['value'] = 0
        self.update_progress()

    def stop(self):
        self.window.after_cancel(self.task_id)
        
    def update_progress(self):
        if self.p['value'] < self.p['maximum']:
            self.p['value'] += 30 
            self.task_id = self.window.after(90, self.update_progress)
        else:
            self.stop()
            self.window.after(500, self.load_next_page)

    def load_next_page(self):
        goToPage(DEarResultPage.DEarResultPage(self.window, self.result_1, self.result_2, self.result_3))

    def drawPage(self):
        self.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/DEarLoadingFrame/image_1.png"))
        self.create_image(
            567.0,
            313.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("control/DEarLoadingFrame/image_2.png"))
        self.create_image(
            567.0,
            392.0,
            image=self.image_image_2
        )

        self.create_text(
            570.0,
            440.0,
            anchor="center",
            text="              Mohon Tunggu Sebentar,\nkami sedang menyiapkannya untuk anda.",
            fill="#FFFFFF",
            font=("Nunito SemiBold", 16 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("control/DEarLoadingFrame/image_3.png"))
        self.create_image(
            1099.3330078125,
            22.33349609375,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("control/DEarLoadingFrame/image_4.png"))
        self.create_image(
            1074.0,
            22.33056640625,
            image=self.image_image_4
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure('blue.Horizontal.TProgressbar', background='#85C13D', troughcolor='#E9F4DA', bordercolor='#E9F4DA')

        self.p = ttk.Progressbar(self.window, orient="horizontal", style='blue.Horizontal.TProgressbar', length=540, mode='determinate')
        self.p.place(x=297, y=381.5, height=21.2)
        self.p['maximum'] = 540  # Set maximum to 100 to represent 100%

        self.start()

        # Start the predictor in a new thread
        self.predictor_thread = threading.Thread(target=self.run_prediction)
        self.predictor_thread.start()


        self.window.mainloop()