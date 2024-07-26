import customtkinter
from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage, NotificationDetailPage

from database.models.Notification import NotificationModel

from datetime import datetime
from dateutil.relativedelta import relativedelta

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

        self.my_frame = customtkinter.CTkScrollableFrame(self.window,
                                                         orientation="vertical",
                                                         width=1028,
                                                         height=370,
                                                         fg_color=BACKGROUND_COLOUR,
                                                         scrollbar_button_color="#404040",
                                                         scrollbar_button_hover_color="#e0e0e0",
                                                         scrollbar_fg_color=BACKGROUND_COLOUR,
                                                         bg_color=BACKGROUND_COLOUR,
                                                         label_fg_color=BACKGROUND_COLOUR,
                                                         border_width=0)

        self.my_frame.place(x=35, y=270)
        self.canvas_scroll = Canvas(self.my_frame, 
                                    width=1028,
                                    height=4000, 
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
    
    def get_date_label(self, notif_datetime):
        today = datetime.now()
        delta = today - notif_datetime
    
        if delta.days == 0:
            return "Today"
        elif delta.days == 1:
            return "1 day ago"
        elif delta.days < 30:
            return f"{delta.days} days ago"
        elif delta.days < 365:
            months = delta.days // 30
            return f"{months} month{'s' if months > 1 else ''} ago"
        else:
            years = delta.days // 365
            return f"{years} year{'s' if years > 1 else ''} ago"
    
    def draw_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    def create_date_label(self, canvas, y_offset, date_label_text):
        x1, y1, x2, y2 = 60, y_offset, 137, y_offset + 30
        self.draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius=10, fill='#ffffff', outline="")
        date_label = Label(canvas, text=date_label_text, bg='#ffffff', font=("Nunito Bold", 10), fg="#9E9E9E")
        canvas.create_window((x1 + x2) // 2, (y1 + y2) // 2, anchor="center", window=date_label)
        return y_offset + 40
    
    def create_notification_card(self, canvas, y_offset, notification, card_bg, card_read_bg, bg_color, goToPage):
        card_btn = Button(canvas, image=card_read_bg if notification['already_read'] else card_bg, 
                          activebackground=BACKGROUND_COLOUR, borderwidth=0, highlightthickness=0, background=BACKGROUND_COLOUR,
                          command=lambda: goToPage(NotificationDetailPage.NotificationDetailPage(self.window, notification)))
        canvas.create_window(48, y_offset, anchor="nw", window=card_btn, width=1034, height=121.63)
    
        header_label = Label(canvas, text=notification['notif_header'], bg=bg_color, fg="#404040", font=("Nunito Bold", 14))
        canvas.create_window(75.51806640625, y_offset + 12.074, anchor="nw", window=header_label)
    
        sub_header_label = Label(canvas, text=notification['notif_subheader'], bg=bg_color, font=("Nunito Regular", 8), fg="#9E9E9E")
        canvas.create_window(75.51806640625, y_offset + 43.074, anchor="nw", window=sub_header_label)
    
        content_label = Label(canvas, text=notification['notif_content'], bg=bg_color, fg="#404040", font=("Nunito Regular", 10))
        canvas.create_window(75.51806640625, y_offset + 72.074, anchor="nw", window=content_label)
    
    def update_cards(self):
        self.canvas_scroll.delete("all")
        card_bg = PhotoImage(file=relative_to_assets("control/NotificationFrame/unread.png"))
        card_read_bg = PhotoImage(file=relative_to_assets("control/NotificationFrame/read.png"))
    
        previous_date_label = None
        y_offset = 0
    
        for i, notification in enumerate(self.data_notifications):
            notif_datetime = notification['notif_datetime']
            bg_color = "#BAED7C" if notification['already_read'] else "#ffffff"
    
            current_date_label = self.get_date_label(notif_datetime)
    
            if current_date_label != previous_date_label:
                y_offset = self.create_date_label(self.canvas_scroll, y_offset, current_date_label)
                previous_date_label = current_date_label
    
            self.create_notification_card(self.canvas_scroll, y_offset, notification, card_bg, card_read_bg, bg_color, goToPage)
            y_offset += 140
    
        self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        self.window.mainloop()

        