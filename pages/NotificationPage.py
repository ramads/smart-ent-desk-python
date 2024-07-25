import customtkinter
from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage, NotificationDetailPage

from database.models.Notification import NotificationModel


class NotificationPage(Canvas, BasePage):

    def __init__(self, window):
        self.window = window
        self.notification = NotificationModel()
        self.temp_data = self.notification.get_notifications()
        self.data_notifications = self.temp_data
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

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_1.png"))
        image_1 = self.create_image(
            565.0,
            201.0,
            image=image_image_1
        )


        image_image_4 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_4.png"))
        image_4 = self.create_image(
            93.3388671875,
            284.869140625,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_5.png"))
        image_5 = self.create_image(
            986.0,
            283.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_6.png"))
        image_6 = self.create_image(
            566.0,
            89.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_7.png"))
        image_7 = self.create_image(
            786.0,
            206.0,
            image=image_image_7
        )

        self.create_text(
            82.0,
            183.0,
            anchor="nw",
            text="Notifikasi",
            fill="#404040",
            font=("Nunito Bold", 25 * -1)
        )

        self.create_text(
            62.35595703125,
            274.894775390625,
            anchor="nw",
            text="Hari ini",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=1034,
                                                         height=320,
                                                         fg_color=BACKGROUND_COLOUR,
                                                         scrollbar_button_color="#bfbfbf",
                                                         scrollbar_button_hover_color="#e0e0e0",
                                                         scrollbar_fg_color=BACKGROUND_COLOUR,
                                                         bg_color=BACKGROUND_COLOUR,
                                                         label_fg_color=BACKGROUND_COLOUR,
                                                         border_width=0)

        self.my_frame.place(x=48, y=315)
        self.canvas_scroll = Canvas(self.my_frame, 
                                    width=1034, 
                                    height=2000, 
                                    bg=BACKGROUND_COLOUR,
                                    highlightthickness=0,
                                    relief="ridge"
                                    )
        self.canvas_scroll.pack()

        self.searchingBox = TextArea(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito Bold", 12),
            placeholder="Enter your text here..."
        )
        self.searchingBox.place(
            x=630.0,
            y=195.0,
            width=315.0,
            height=30.0
        )

        inactive_button_1 = relative_to_assets("control/NotificationFrame/button_1.png")
        active_button_1 = relative_to_assets("control/NotificationFrame/active_button_1.png")

        inactive_button_2 = relative_to_assets("control/NotificationFrame/button_2.png")
        active_button_2 = relative_to_assets("control/NotificationFrame/active_button_2.png")
        
        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0, 
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(HomePage.HomePage(self.window)))
        
        create_hover_button(self.window, 960.0, 183.0, 88.0, 45.0, 
                            '#FFFFFF', inactive_button_2, active_button_2, 
                            lambda: self.searching())        


        self.update_cards()

    def searching(self):
        input_text = self.searchingBox.get("1.0", "end-1c").lower().strip()
        input_text = input_text.replace("\n", "").replace("\t", "").replace(" ", "")
        print(input_text)
        if input_text == "" or input_text == "enteryourtexthere...":
            self.data_notifications = self.temp_data
        else:
            self.data_notifications = [
                item for item in self.temp_data if input_text in item['notif_header'].lower().replace(" ", "")
            ]

        self.update_cards()


    def update_cards(self):
        self.canvas_scroll.delete("all")
        card_bg = PhotoImage(file=relative_to_assets("control/NotificationFrame/image_2.png"))
        card_read_bg = PhotoImage(file=relative_to_assets("control/NotificationFrame/image_3.png"))



        for i in range(len(self.data_notifications)):
            y_offset = i * 130
            bg_color = "#BAED7C" if self.data_notifications[i]['already_read'] else "#ffffff"
            card_btn = Button(self.canvas_scroll, image=card_read_bg if self.data_notifications[i]['already_read'] else card_bg, 
                              activebackground=BACKGROUND_COLOUR, borderwidth=0, highlightthickness=0, background=BACKGROUND_COLOUR,
                        command=lambda i=i: goToPage(NotificationDetailPage.NotificationDetailPage(self.window, self.data_notifications[i])))
            btn_window = self.canvas_scroll.create_window(48, 307.37 + y_offset, anchor="nw", window=card_btn,
                                            width=1034, height=121.63)

            header_label = Label(self.canvas_scroll, text=self.data_notifications[i]['notif_header'], bg=bg_color, font=("Nunito Bold", 16))
            self.canvas_scroll.create_window(75.51806640625, 319.444091796875 + y_offset, anchor="nw", window=header_label)

            sub_header_label = Label(self.canvas_scroll, text=self.data_notifications[i]['notif_subheader'], bg=bg_color, font=("Nunito Regular", 10), fg="#9E9E9E")
            self.canvas_scroll.create_window(75.51806640625, 349.444091796875 + y_offset, anchor="nw", window=sub_header_label)

            content_label = Label(self.canvas_scroll, text=self.data_notifications[i]['notif_content'], bg=bg_color, font=("Nunito Regular", 12))
            self.canvas_scroll.create_window(75.51806640625, 379.444091796875 + y_offset, anchor="nw", window=content_label)

        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        self.window.mainloop()

        