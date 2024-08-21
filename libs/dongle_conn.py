import time
import serial
import requests
from config import DONGLE_PORT_ADR, SERVER_URL

class DongleCom():
    def __init__(self):
        self.com = None

    def connect(self):
        self.com = None
        setup = False
        prev = time.time()
        while not setup:
            try:
                self.com = serial.Serial(DONGLE_PORT_ADR, 115200, timeout=1)
            except:
                if time.time() - prev > 0.5:  # waiting time
                    print("No dongle detected, please plug your dongle")
                    break

            if self.com is not None:  # We're connected
                print("Dongle Connected!")
                setup = True
                return True
        return False

    def read_serial(self, num_char=32):
        if self.com is not None:
            encrypted_string = self.com.read(num_char)
            return encrypted_string.decode()
        return None

    def send_to_server(self, encrypted_string):
        try:
            response = requests.post(SERVER_URL, json={"encrypted_string": encrypted_string})
            response_data = response.json()
            return response_data.get("is_registered", False)
        except Exception as e:
            print(f"Error sending data to server: {e}")
            return False

    def check_dongle_registration(self):
        if self.connect():
            encrypted_string = self.read_serial()
            print("Encrypted Dongle String:", encrypted_string)
            if encrypted_string:
                is_registered = self.send_to_server(encrypted_string)
                if is_registered:
                    print("Dongle is registered.")
                    return True
                else:
                    print("Dongle is not registered.")
                    return False
        else:
            print("Unable to connect to dongle.")
            return False

# Example usage
if __name__ == "__main__":
    dongle_com = DongleCom()
    if not dongle_com.check_dongle_registration():
        print("Application will not start as the dongle is not registered.")
        # Add logic to prevent application startup here
