import customtkinter
from tkinter import *
from colors import *
from helpers import *
from notificationBar import notificationBar

from pages import HomePage

class MedicalRecordPage(Canvas, BasePage):

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

    def drawPage(self):
        self.place(x=0, y=0)

        wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            413.0,
            image=image_image_1
        )

        my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                    orientation="vertical",
                                                    width=955,
                                                    height=300,
                                                    fg_color="#FFFFFF",
                                                    scrollbar_button_hover_color="#404040",
                                                    scrollbar_fg_color="#F3F3F3",
                                                    bg_color="#FFFFFF",
                                                    border_width=0)

        my_frame.place(x=75, y=305)
        # Create a canvas within the scrollable frame
        canvas_scroll = Canvas(my_frame, width=955, height=2000, bg="#FFFFFF")
        canvas_scroll.pack()

        button_images = []

        for i in range(50):
            y_offset = i * 50
            canvas_scroll.create_rectangle(81.0, 367.0 + y_offset, 1278.0, 367.0 + y_offset, fill="#F3F3F3", outline="")
            # canvas_scroll.create_rectangle(81.0, 318.0 + y_offset, 1278.0, 318.0 + y_offset, fill="#F3F3F3", outline="")
            canvas_scroll.create_text(81.0, 322.0 + y_offset, anchor="nw", text="Alma Liakua Mutia", fill="#404040",
                                      font=("Nunito Regular", 20 * -1))
            canvas_scroll.create_text(380, 322.0 + y_offset, anchor="nw", text="OMA Perforasi", fill="#404040",
                                      font=("Nunito Regular", 20 * -1))
            canvas_scroll.create_text(650, 322.0 + y_offset, anchor="nw", text="16 December 2023", fill="#404040",
                                      font=("Nunito Regular", 20 * -1))

            button_image_1 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/button_1.png"))
            button_images.append(button_image_1)
            button_1 = Button(canvas_scroll, image=button_image_1, borderwidth=0, highlightthickness=0,
                              command=lambda: print("button_1 clicked"), relief="flat")
            canvas_scroll.create_window(914.22119140625, 329.20361328125 + y_offset, anchor="nw", window=button_1,
                                        width=23.592920303344727, height=23.592920303344727)

            button_image_2 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/button_2.png"))
            button_images.append(button_image_2)
            button_2 = Button(canvas_scroll, image=button_image_2, borderwidth=0, highlightthickness=0,
                              command=lambda: print("button_2 clicked"), relief="flat")
            canvas_scroll.create_window(942.814208984375, 329.20361328125 + y_offset, anchor="nw", window=button_2,
                                        width=23.592920303344727, height=23.592920303344727)

            button_image_3 = PhotoImage(file=relative_to_assets("control/MedicalRecordFrame/button_3.png"))
            button_images.append(button_image_3)
            button_3 = Button(canvas_scroll, image=button_image_3, borderwidth=0, highlightthickness=0,
                              command=lambda: print("button_3 clicked"), relief="flat")
            canvas_scroll.create_window(971.406982421875, 329.20361328125 + y_offset, anchor="nw", window=button_3,
                                        width=23.592920303344727, height=23.592920303344727)

        canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))

        self.create_text(
            81.0,
            273.0,
            anchor="nw",
            text="Nama",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            380,
            273.0,
            anchor="nw",
            text="Diagnosa",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            650.0,
            273.0,
            anchor="nw",
            text="Tanggal Periksa",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        self.create_text(
            915.0,
            273.0,
            anchor="nw",
            text="Action",
            fill="#404040",
            font=("Nunito Bold", 20 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_4.png"))
        image_4 = self.create_image(
            566.0,
            89.0,
            image=image_image_4
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

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_5.png"))
        image_5 = self.create_image(
            89.0,
            139.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/image_6.png"))
        image_6 = self.create_image(
            790.0,
            239.0,
            image=image_image_6
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordFrame/button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=964.0,
            y=216.0,
            width=88.0,
            height=45.0
        )

        self.create_text(
            81.0,
            216.0,
            anchor="nw",
            text="Riwayat Pasien",
            fill="#404040",
            font=("Nunito Bold", 25 * -1)
        )

        inactive_button_4 = relative_to_assets("control/MedicalRecordFrame/button_4.png")
        active_button_4 = relative_to_assets("control/MedicalRecordFrame/active_button_4.png")

        
        create_hover_button(self.window, 471.0,662.0, 192.0, 54.0, 
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: goToPage(HomePage.HomePage(self.window)))
        
        self.window.mainloop()