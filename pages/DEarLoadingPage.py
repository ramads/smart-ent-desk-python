import threading
from tkinter import *
from tkinter import ttk
from colors import *
from helpers import *
from notificationBar import notificationBar

from pages import DEarResultPage
from machine_learning.image_predictor import ImagePredictor


class DEarLoadingPage(Canvas, BasePage):
    result_1 = ("",0)
    result_2 = ("",0)
    result_3 = ("",0)

    def __init__(self, window, temp_data):
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
            self.window.after(100, self.check_thread)

    def check_thread(self):
        if self.predictor_thread.is_alive():
            self.window.after(5, self.check_thread)
        else:
            goToPage(DEarResultPage.DEarResultPage(self.window, self.temp_data))

    def drawPage(self):
        self.place(x=0, y=0)

        wifi_clock_app = notificationBar(self.window)

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