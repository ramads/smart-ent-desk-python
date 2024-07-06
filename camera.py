import cv2
import threading
from tkinter import *
from PIL import Image, ImageTk
import os

os.makedirs('image_capture', exist_ok=True)

# Initialize Tkinter window
window = Tk()
window.title("Camera Access Example")
window.geometry("1512x982")

# Global variables for video capture
vidCap = cv2.VideoCapture(0)
ret, frame = vidCap.read()
if not ret:
    print("Failed to grab frame")
    exit()

# Function to update the camera frame
def update_frame():
    global ret, frame, canvas, captured_image
    ret, frame = vidCap.read()
    if ret:
        frame = cv2.resize(frame, (1160, 596))
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = ImageTk.PhotoImage(image=Image.fromarray(opencv_image))
        canvas.create_image(806.0, 398.0, image=captured_image)
    canvas.after(10, update_frame)

# Function to handle image capture
def onCapture(patient_id, patient_name):
    global frame
    if frame is not None:
        filename = os.path.join('image_capture', f"{patient_id}-{patient_name}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image captured and saved as '{filename}'")

# Function to create camera page UI
def openCameraPage():
    global canvas, captured_image

    canvas = Canvas(
        window,
        bg="#DFEBD0",
        height=982,
        width=1512,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Add a button for capturing the image
    capture_button = Button(
        window,
        text="Capture Image",
        command=lambda: onCapture(patient_id.get(), patient_name.get().replace(" ", "_")),
        relief="flat"
    )
    capture_button.place(x=700, y=900)

    # Dynamic input test
    patient_id_label = Label(window, text="Patient ID:")
    patient_id_label.place(x=600, y=850)
    patient_id = Entry(window)
    patient_id.place(x=670, y=850)

    patient_name_label = Label(window, text="Patient Name:")
    patient_name_label.place(x=800, y=850)
    patient_name = Entry(window)
    patient_name.place(x=890, y=850)

    canvas.after(10, update_frame)

# Start the camera page in a separate thread
def start_camera_thread():
    camera_thread = threading.Thread(target=openCameraPage)
    camera_thread.start()

# Initialize and start the camera thread
start_camera_thread()

window.mainloop()

# Release the video capture object when done
vidCap.release()
cv2.destroyAllWindows()