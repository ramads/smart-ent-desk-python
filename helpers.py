from pathlib import Path
from tkinter import Button, PhotoImage
from pages.BasePage import BasePage

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