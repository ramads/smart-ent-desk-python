import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import subprocess
import platform
import re
import time
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/control/notificationBar")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class notificationBar:
    def __init__(self, root):
        self.root = root

        # Load Wi-Fi strength images
        self.wifi_images = []
        image_names = [relative_to_assets('wifi_disconnected.png'), relative_to_assets('wifi_1.png'),
                       relative_to_assets('wifi_2.png'), relative_to_assets('wifi_3.png'),
                       relative_to_assets('wifi_no_internet.png')]
        for image_name in image_names:
            image = Image.open(image_name)
            self.wifi_images.append(ImageTk.PhotoImage(image))

        # Create a label to display the Wi-Fi image
        self.wifi_image_label = Label(self.root, bg='#85C13F')
        self.wifi_image_label.place(x=1020.0, y=10.0, width=65, height=30)

        # Create a label to display the time
        self.clock_label = Label(self.root, text="", font=("Nunito Bold", 12), fg='white', bg='#85C13F')
        self.clock_label.place(x=20.0, y=13.0, width=65, height=21)

        # Start updating the Wi-Fi strength and time
        self.update_wifi_strength()
        self.update_time()

    def get_wifi_strength(self):
        os_name = platform.system()

        if os_name == "Windows":
            result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True).stdout
            match = re.search(r'Signal\s*:\s*(\d+)%', result)
            if match:
                return int(match.group(1))
            else:
                return None

        elif os_name == "Linux":
            result = subprocess.run(["iwconfig"], capture_output=True, text=True).stdout
            match = re.search(r'Signal level=(-\d+)', result)
            if match:
                signal_level = int(match.group(1))
                max_signal_level = -30
                min_signal_level = -90
                signal_strength = 100 * (signal_level - min_signal_level) / (max_signal_level - min_signal_level)
                return int(signal_strength)
            else:
                return None

    def is_connected_to_internet(self):
        try:
            subprocess.run(["ping", "-c", "1", "8.8.8.8"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def update_wifi_strength(self):
        strength = self.get_wifi_strength()
        connected_to_internet = self.is_connected_to_internet()

        if strength is not None:
            if connected_to_internet:
                self.update_wifi_animation(strength)
            else:
                self.update_wifi_animation(-1)
        else:
            self.update_wifi_animation(-2)

        self.root.after(5000, self.update_wifi_strength)

    def update_wifi_animation(self, strength):
        if strength >= 80:
            self.wifi_image_label.config(image=self.wifi_images[3])
        elif strength >= 40:
            self.wifi_image_label.config(image=self.wifi_images[2])
        elif strength > 0:
            self.wifi_image_label.config(image=self.wifi_images[1])
        elif strength == -1:
            self.wifi_image_label.config(image=self.wifi_images[4])
        else:
            self.wifi_image_label.config(image=self.wifi_images[0])

    def update_time(self):
        current_time = time.strftime('%H:%M')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)
