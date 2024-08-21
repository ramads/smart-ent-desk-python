from pathlib import Path
from tkinter import Button, PhotoImage
from pages.BasePage import BasePage
import tkinter as tk
import cv2
import numpy as np
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


def crop_and_save(img, zoom_ratio, target_size):
    # Tentukan sisi terpendek untuk menentukan ukuran cropping, agar dapat menghasilkan ratio 1x1
    height, width, _ = img.shape
    crop_size = min(height, width)

    # Hitung koordinat untuk crop agar gambar berada di tengah
    x_center, y_center = width // 2, height // 2
    x1 = x_center - crop_size // 2
    y1 = y_center - crop_size // 2
    x2 = x_center + crop_size // 2
    y2 = y_center + crop_size // 2

    # Crop gambar
    cropped_image = img[y1:y2, x1:x2]

    # Hitung ukuran baru setelah pembesaran
    zoomed_width = int(crop_size * zoom_ratio)
    zoomed_height = int(crop_size * zoom_ratio)

    # Resize gambar hasil crop ke ukuran yang lebih besar
    zoomed_image = cv2.resize(cropped_image, (zoomed_width, zoomed_height), interpolation=cv2.INTER_LINEAR)
    target_width, target_height = target_size

    # Buat image dengan background hitam jika hasil zoom lebih kecil dari target size
    output_image = np.zeros((target_height, target_width, 3), dtype=np.uint8)

    # Hitung posisi tengah dari gambar hasil pembesaran
    x_offset = (target_width - zoomed_width) // 2
    y_offset = (target_height - zoomed_height) // 2 + 20  # Geser gambar 100 piksel ke bawah

    # Pastikan offset tidak menyebabkan gambar keluar dari batas target
    if y_offset + zoomed_height > target_height:
        y_offset = target_height - zoomed_height

    # Jika gambar hasil pembesaran lebih besar dari target size, crop lagi
    if zoomed_width > target_width or zoomed_height > target_height:
        x1 = max((zoomed_width - target_width) // 2, 0)
        y1 = max((zoomed_height - target_height) // 2, 0)
        x2 = x1 + target_width
        y2 = y1 + target_height
        output_image = zoomed_image[y1:y2, x1:x2]
    else:
        output_image[y_offset:y_offset + zoomed_height, x_offset:x_offset + zoomed_width] = zoomed_image

    return output_image

def crop_with_padding(img, zoom_ratio, target_size):
    height, width, _ = img.shape

    new_width = width // zoom_ratio
    new_height = height // zoom_ratio

    # Calculate coordinates
    x_center, y_center = width // 2, height // 2

    # Calculate crop coordinates
    x1 = max(int(x_center - new_width // 2), 0)
    y1 = max(int(y_center - new_height // 2), 0)
    x2 = min(int(x_center + new_width // 2), width)
    y2 = min(int(y_center + new_height // 2), height)

    # Potong sesuai ratio zoom
    cropped_frame = img[y1:y2, x1:x2]

    # Resize sesuai target gambar
    target_width, target_height = target_size

    # Add black padding, biar ratio image tetap
    padded_image = np.zeros((target_height, target_width, 3), dtype=np.uint8)

    # Calculate Scaling Factors
    scale_width = target_width / cropped_frame.shape[1]
    scale_height = target_height / cropped_frame.shape[0]
    scale = min(scale_width, scale_height)  # Choose the smaller scale to maintain aspect ratio

    # Calculate new dimensions for resized image
    resized_width = int(cropped_frame.shape[1] * scale)
    resized_height = int(cropped_frame.shape[0] * scale)

    # Resize gambar sesuai target dan tidak merubah ratio ukuran
    resized_frame = cv2.resize(cropped_frame, (resized_width, resized_height), interpolation=cv2.INTER_LINEAR)

    # Atur posisi gambar ke tenga-tengah
    x_offset = (target_width - resized_width) // 2
    y_offset = (target_height - resized_height) // 2

    padded_image[y_offset:y_offset + resized_height, x_offset:x_offset + resized_width] = resized_frame

    return padded_image

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