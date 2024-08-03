from pathlib import Path
from tkinter import Button, PhotoImage
from pages.BasePage import BasePage
import tkinter as tk
import cv2
import threading

# default ukuran window
DEFAULT_APP_VIEW_GEOMETRY = "1512x982"
DEFAULT_APP_CONTROL_GEOMETRY = "1133x744"

APP_TITLE = "Smart ENT"
DIR_TEMP_IMAGE = "temp_image"

def relative_to_assets(path: str) -> Path: #
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")
    return ASSETS_PATH / Path(path)

def relative_to_image_capture(path: str) -> Path: #
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./" + DIR_TEMP_IMAGE)
    return ASSETS_PATH / Path(path)

def goToPage(page:BasePage, data=None):
    if data is None:
        page.drawPage()
    else:
        page.drawPage(data)

def create_hover_button(window, x, y, width, height, bg_color, image_path, hover_image_path, command):
    button_image = PhotoImage(file=relative_to_assets(image_path))
    hover_button_image = PhotoImage(file=relative_to_assets(hover_image_path))
    
    button = Button(
        window,
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=command,
        relief="flat",
        activebackground=bg_color,
        bg=bg_color
    )
    
    def on_enter(event):
        button.config(image=hover_button_image)
    
    def on_leave(event):
        button.config(image=button_image)
    
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.place(x=x, y=y, width=width, height=height)
    button.image = button_image
    button.hover_image = hover_button_image

    return button

def crop_image(img, ratio):
    # Calculate coordinate and zoom ratio
    height, width, _ = img.shape
    new_width, new_height = width // ratio, height // ratio  # zoom ratio
    x_center, y_center = width // 2, height // 2
    x1, y1 = int(x_center - new_width // 2), int(y_center - new_height // 2)
    x2, y2 = int(x_center + new_width // 2), int(y_center + new_height // 2)

    # Crop image
    cropped_frame = img[y1:y2, x1:x2]

    # Resize back to original size for zoom effect
    zoomed_frame = cv2.resize(cropped_frame, (width, height))

    return zoomed_frame

class TextArea(tk.Text):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self.cget("fg")

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0.0, self.placeholder)
        self.config(fg=self.placeholder_color)

    def foc_in(self, *args):
        if self.get(0.0, "end-1c") == self.placeholder:
            self.delete(0.0, "end")
            self.config(fg=self.default_fg_color)

    def foc_out(self, *args):
        if not self.get(0.0, "end-1c"):
            self.put_placeholder()