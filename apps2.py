
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1495x982")
# window.attributes('-fullscreen',True)
window.configure(bg = "#DFEBD0")
window.title("Smart ENT v0.1.")

def switchPage(page, data = None):
    if data is None:
        page()
    else:
        page(data)

# Frame Home
def home_page():
    canvas = Canvas(
        window,
        bg="#85C13D",
        height=982,
        width=1495,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("home2/image_1.png"))
    image_1 = canvas.create_image(
        101.0,
        192.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("home2/image_2.png"))
    image_2 = canvas.create_image(
        1418.2763671875,
        32.8797607421875,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("home2/image_3.png"))
    image_3 = canvas.create_image(
        1374.1884765625,
        31.87451171875,
        image=image_image_3
    )

    canvas.create_text(
        27.7095947265625,
        18.2392578125,
        anchor="nw",
        text="9:41",
        fill="#FFFFFF",
        font=("Nunito Bold", 19 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("home2/image_4.png"))
    image_4 = canvas.create_image(
        747.0,
        100.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("home2/button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=diagnosis_page),
        relief="flat"
    )
    button_1.place(
        x=64.0,
        y=291.0,
        width=576.0,
        height=436.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("home2/button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=670.0,
        y=291.0,
        width=362.0,
        height=434.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("home2/button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=1061.0,
        y=293.0,
        width=367.0,
        height=205.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("home2/button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=1061.0,
        y=522.0,
        width=367.0,
        height=205.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("home2/button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=776.0,
        y=798.0,
        width=326.0,
        height=118.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("home2/button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=393.0,
        y=798.0,
        width=328.0,
        height=118.0
    )

    canvas.create_text(
        155.0,
        199.0,
        anchor="nw",
        text="Unit THT",
        fill="#F1F1F1",
        font=("Nunito SemiBold", 17 * -1)
    )

    canvas.create_text(
        155.0,
        163.0,
        anchor="nw",
        text="RS. Universitas Mataram",
        fill="#FFFFFF",
        font=("Nunito Black", 21 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


def diagnosis_page():
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

    btnNavBackground = PhotoImage(file=relative_to_assets("btn_nav_background.png"))
    image_1 = canvas.create_image(
        84.0,
        491.0,
        image=btnNavBackground
    )

    backActiveBtn = PhotoImage(
        file=relative_to_assets("btn_active_background.png"))
    image_2 = canvas.create_image(
        78.0,
        176.0,
        image=backActiveBtn
    )

    settingIcon = PhotoImage(file=relative_to_assets("icon_setting.png"))
    btnSetting = Button(
        image=settingIcon,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnSetting clicked"),
        relief="flat"
    )
    btnSetting.place(
        x=62.0,
        y=236.0,
        width=34.0,
        height=34.0
    )

    iconBtnHome = PhotoImage(file=relative_to_assets("icon_btn_home.png"))
    btnHome = Button(
        image=iconBtnHome,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=home_page),
        relief="flat"
    )
    btnHome.place(
        x=62.0,
        y=159.0,
        width=35.0,
        height=35.0
    )

    iconBtnPref = PhotoImage(file=relative_to_assets("icon_btn_setting2.png"))
    btnPref = Button(
        image=iconBtnPref,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnPref clicked"),
        relief="flat"
    )
    btnPref.place(
        x=61.0,
        y=806.0,
        width=35.0,
        height=35.0
    )

    iconBtnNotif = PhotoImage(file=relative_to_assets("icon_btn_notif.png"))
    btnNotif = Button(
        image=iconBtnNotif,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnNotif clicked"),
        relief="flat"
    )
    btnNotif.place(
        x=64.0,
        y=68.0,
        width=28.0,
        height=28.0
    )

    iconBtnExit = PhotoImage(
        file=relative_to_assets("icon_btn_exit.png"))
    btnExit = Button(
        image=iconBtnExit,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button exit clicked"),
        relief="flat"
    )
    btnExit.place(
        x=64.0,
        y=884.0,
        width=28.0,
        height=28.0
    )

    iconBtnPasien = PhotoImage(
        file=relative_to_assets("icon_btn_pasien.png"))
    btnPasien = Button(
        image=iconBtnPasien,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button pasien clicked"),
        relief="flat"
    )
    btnPasien.place(
        x=60.0,
        y=309.0,
        width=38.0,
        height=38.0
    )

    iconBtnInfo = PhotoImage(
        file=relative_to_assets("icon_btn_info.png"))
    btnInfo = Button(
        image=iconBtnInfo,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button info clicked"),
        relief="flat"
    )
    btnInfo.place(
        x=61.0,
        y=745.0,
        width=35.0,
        height=35.0
    )

    canvas.create_rectangle(
        46.0,
        120.0,
        113.0,
        120.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        46.0,
        860.0,
        113.0,
        860.0,
        fill="#FFFFFF",
        outline="")

    # background button togle control

    image_image_3 = PhotoImage(
        file=relative_to_assets("frame_background_ear.png"))
    image_3 = canvas.create_image(
        396.0,
        717.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("img_banner.png"))
    image_4 = canvas.create_image(
        815.0,
        279.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("frame_background_nose.png"))
    image_5 = canvas.create_image(
        815.0,
        717.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("frame_background_null.png"))
    image_6 = canvas.create_image(
        1234.0,
        718.0,
        image=image_image_6
    )

    iconBtnStart = PhotoImage(file=relative_to_assets("icon_btn_start.png"))
    btnEarDiagnose = Button(
        image=iconBtnStart,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=preparingCamera),
        relief="flat"
    )
    btnEarDiagnose.place(
        x=243.0,
        y=834.0,
        width=280.0,
        height=42.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("icon_btn_start2.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=662.0,
        y=834.0,
        width=280.0,
        height=42.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("icon_btn_start3.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=1081.0,
        y=835.0,
        width=280.0,
        height=42.0
    )

    canvas.create_text(
        225.0,
        753.0,
        anchor="nw",
        text="Lorem ipsum dolor sit amet",
        fill="#9E9E9E",
        font=("Nunito SemiBold", 14 * -1)
    )

    canvas.create_text(
        225.0,
        705.0,
        anchor="nw",
        text="Diagnosa Telinga",
        fill="#404040",
        font=("Nunito Bold", 19 * -1)
    )

    canvas.create_text(
        644.0,
        705.0,
        anchor="nw",
        text="Diagnosa Hidung",
        fill="#404040",
        font=("Nunito Bold", 19 * -1)
    )

    canvas.create_text(
        644.0,
        753.0,
        anchor="nw",
        text="Lorem ipsum dolor sit amet",
        fill="#9E9E9E",
        font=("Nunito SemiBold", 14 * -1)
    )

    canvas.create_text(
        1063.0,
        754.0,
        anchor="nw",
        text="Lorem ipsum dolor sit amet",
        fill="#9E9E9E",
        font=("Nunito SemiBold", 14 * -1)
    )

    canvas.create_text(
        1063.0,
        706.0,
        anchor="nw",
        text="Diagnosa Tenggorokan",
        fill="#404040",
        font=("Nunito Bold", 19 * -1)
    )

    window.resizable(False, False)
    window.mainloop()


import cv2
vidCap = cv2.VideoCapture()

def preparingCamera():
    # Declare the width and height in variables
    width, height = 1160, 596

    # Set the width and height
    vidCap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vidCap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    vidCap.open(0)
    openCameraPage()

def onStopCamera():
    vidCap.release()
    switchPage(page=home_page)

def onCaptured(image):
    vidCap.release()
    switchPage(page=diagnose_ear_image_page, data=image)

def openCameraPage():
    # Capture the video frame by frame
    _, frame = vidCap.read()

    frame = cv2.resize(frame, (1160, 596))

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

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
    btnNavBackground = PhotoImage(file=relative_to_assets("btn_nav_background.png"))
    image_1 = canvas.create_image(
        84.0,
        491.0,
        image=btnNavBackground
    )

    backActiveBtn = PhotoImage(
        file=relative_to_assets("btn_active_background.png"))
    image_2 = canvas.create_image(
        78.0,
        176.0,
        image=backActiveBtn
    )

    settingIcon = PhotoImage(file=relative_to_assets("icon_setting.png"))
    btnSetting = Button(
        image=settingIcon,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnSetting clicked"),
        relief="flat"
    )
    btnSetting.place(
        x=62.0,
        y=236.0,
        width=34.0,
        height=34.0
    )

    iconBtnHome = PhotoImage(file=relative_to_assets("icon_btn_home.png"))
    btnHome = Button(
        image=iconBtnHome,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=onStopCamera),
        relief="flat"
    )
    btnHome.place(
        x=62.0,
        y=159.0,
        width=35.0,
        height=35.0
    )

    iconBtnPref = PhotoImage(file=relative_to_assets("icon_btn_setting2.png"))
    btnPref = Button(
        image=iconBtnPref,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnPref clicked"),
        relief="flat"
    )
    btnPref.place(
        x=61.0,
        y=806.0,
        width=35.0,
        height=35.0
    )

    iconBtnNotif = PhotoImage(file=relative_to_assets("icon_btn_notif.png"))
    btnNotif = Button(
        image=iconBtnNotif,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("btnNotif clicked"),
        relief="flat"
    )
    btnNotif.place(
        x=64.0,
        y=68.0,
        width=28.0,
        height=28.0
    )

    iconBtnExit = PhotoImage(
        file=relative_to_assets("icon_btn_exit.png"))
    btnExit = Button(
        image=iconBtnExit,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button exit clicked"),
        relief="flat"
    )
    btnExit.place(
        x=64.0,
        y=884.0,
        width=28.0,
        height=28.0
    )

    iconBtnPasien = PhotoImage(
        file=relative_to_assets("icon_btn_pasien.png"))
    btnPasien = Button(
        image=iconBtnPasien,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button pasien clicked"),
        relief="flat"
    )
    btnPasien.place(
        x=60.0,
        y=309.0,
        width=38.0,
        height=38.0
    )

    iconBtnInfo = PhotoImage(
        file=relative_to_assets("icon_btn_info.png"))
    btnInfo = Button(
        image=iconBtnInfo,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button info clicked"),
        relief="flat"
    )
    btnInfo.place(
        x=61.0,
        y=745.0,
        width=35.0,
        height=35.0
    )

    canvas.create_rectangle(
        46.0,
        120.0,
        113.0,
        120.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        46.0,
        860.0,
        113.0,
        860.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        820.0,
        490.0,
        image=image_image_1
    )

    # Capture the latest frame and transform to image
    captured_image = ImageTk.PhotoImage(image=Image.fromarray(opencv_image))
    image_2 = canvas.create_image(
        806.0,
        398.0,
        image=captured_image
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("btn_back.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=onStopCamera),
        relief="flat"
    )
    button_1.place(
        x=667.5,
        y=828.0,
        width=136.0,
        height=42.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("btn_capture.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: onCaptured(captured_image),
        relief="flat"
    )
    button_2.place(
        x=811.5,
        y=828.0,
        width=136.0,
        height=42.0
    )

    canvas.create_text(
        234.0,
        736.0,
        anchor="nw",
        text="Diagnosa Telinga",
        fill="#404040",
        font=("Nunito Bold", 24 * -1)
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("icon_btn_info.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=61.0,
        y=745.0,
        width=35.0,
        height=35.0
    )

    canvas.create_text(
        234.0,
        784.0,
        anchor="nw",
        text="Sebelum mengambil gambar silakan ambil Otoscope dan pastikan sudah diarahkan dengan benar.",
        fill="#14181F",
        font=("Nunito Regular", 14 * -1)
    )

    canvas.after(10, openCameraPage)

    window.resizable(False, False)
    window.mainloop()


def diagnose_ear_image_page(capturedImage):
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
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        820.0,
        490.0,
        image=image_image_1
    )

    # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        806.0,
        398.0,
        image=capturedImage
    )

    btnBack = PhotoImage(
        file=relative_to_assets("btn_recapture.png"))
    button_1 = Button(
        image=btnBack,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=preparingCamera),
        relief="flat"
    )
    button_1.place(
        x=667.5,
        y=828.0,
        width=136.0,
        height=42.0
    )

    btnDiagnose = PhotoImage(
        file=relative_to_assets("btn_pro_diagnose.png"))
    button_2 = Button(
        image=btnDiagnose,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(result_diagnose_page, data=capturedImage),
        relief="flat"
    )
    button_2.place(
        x=811.5,
        y=828.0,
        width=136.0,
        height=42.0
    )

    # canvas.create_text(
    #     234.0,
    #     736.0,
    #     anchor="nw",
    #     text="Diagnosa Telinga",
    #     fill="#404040",
    #     font=("Nunito Bold", 24 * -1)
    # )

    # background button toggle controller
    # image_image_3 = PhotoImage(
    #     file=relative_to_assets("image_3.png"))
    # image_3 = canvas.create_image(
    #     1324.0,
    #     647.0,
    #     image=image_image_3
    # )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        84.0,
        491.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        78.0,
        176.0,
        image=image_image_5
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=62.0,
        y=236.0,
        width=34.0,
        height=34.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=62.0,
        y=159.0,
        width=35.0,
        height=35.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=61.0,
        y=806.0,
        width=35.0,
        height=35.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=64.0,
        y=68.0,
        width=28.0,
        height=28.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=64.0,
        y=884.0,
        width=28.0,
        height=28.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=60.0,
        y=309.0,
        width=38.0,
        height=38.0
    )

    canvas.create_rectangle(
        46.0,
        120.0,
        113.0,
        120.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        46.0,
        860.0,
        113.0,
        860.0,
        fill="#FFFFFF",
        outline="")

    button_image_9 = PhotoImage(
        file=relative_to_assets("icon_btn_info.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=61.0,
        y=745.0,
        width=35.0,
        height=35.0
    )

    canvas.create_text(
        234.0,
        736.0,
        anchor="nw",
        text="Gambar Berhasil Diambil",
        fill="#404040",
        font=("Nunito Bold", 24 * -1)
    )

    # button_image_10 = PhotoImage(
    #     file=relative_to_assets("icon_btn_start3.png"))
    # button_10 = Button(
    #     image=button_image_10,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_10 clicked"),
    #     relief="flat"
    # )
    # button_10.place(
    #     x=1304.0,
    #     y=625.0,
    #     width=42.0,
    #     height=42.0
    # )


    window.resizable(False, False)
    window.mainloop()

def result_diagnose_page(capturedImage):
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
    image_image_1 = PhotoImage(
        file=relative_to_assets("frame7/image_1.png"))
    image_1 = canvas.create_image(
        618.0,
        327.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("frame7/image_2.png"))
    image_2 = canvas.create_image(
        1245.0,
        327.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("frame7/image_3.png"))
    image_3 = canvas.create_image(
        821.0,
        773.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("frame7/image_4.png"))
    image_4 = canvas.create_image(
        84.0,
        491.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("frame7/image_5.png"))
    image_5 = canvas.create_image(
        78.0,
        176.0,
        image=image_image_5
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("frame7/button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=62.0,
        y=236.0,
        width=34.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("frame7/button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switchPage(page=home_page),
        relief="flat"
    )
    button_2.place(
        x=62.0,
        y=159.0,
        width=35.0,
        height=35.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("frame7/button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=61.0,
        y=806.0,
        width=35.0,
        height=35.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("frame7/button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=64.0,
        y=68.0,
        width=28.0,
        height=28.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("frame7/button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=64.0,
        y=884.0,
        width=28.0,
        height=28.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("frame7/button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=60.0,
        y=309.0,
        width=38.0,
        height=38.0
    )

    canvas.create_rectangle(
        46.0,
        120.0,
        113.0,
        120.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        46.0,
        860.0,
        113.0,
        860.0,
        fill="#FFFFFF",
        outline="")

    button_image_7 = PhotoImage(
        file=relative_to_assets("frame7/button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=61.0,
        y=745.0,
        width=35.0,
        height=35.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("frame7/button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=234.0,
        y=861.0,
        width=136.0,
        height=42.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("frame7/button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=378.0,
        y=861.0,
        width=136.0,
        height=42.0
    )

    canvas.create_text(
        234.0,
        821.0,
        anchor="nw",
        text="Pastikan data yang dimunculkan sesuai dengan kondisi sebenarnya.",
        fill="#151920",
        font=("Nunito Regular", 12 * -1)
    )

    canvas.create_text(
        234.0,
        785.0,
        anchor="nw",
        text="Tingkat keyakinan dignosa: 65%",
        fill="#404040",
        font=("Nunito Regular", 14 * -1)
    )

    canvas.create_text(
        234.0,
        748.0,
        anchor="nw",
        text="OMA Perofrasi adalah gangguan ........ . Dicirikan dengan .......",
        fill="#404040",
        font=("Nunito SemiBold", 16 * -1)
    )

    canvas.create_text(
        234.0,
        704.0,
        anchor="nw",
        text="OMA PERFORASI",
        fill="#1E5C2A",
        font=("Nunito Bold", 30 * -1)
    )

    canvas.create_text(
        234.0,
        644.0,
        anchor="nw",
        text="Hasil Diagnosa",
        fill="#404040",
        font=("Nunito Bold", 24 * -1)
    )

    # image_image_6 = PhotoImage(file=relative_to_assets("frame7/image_6.png"))
    # img = ImageTk.getimage(capturedImage)
    # img.resize((759, 464))

    # new_width = 759
    # new_height = 464
    # old_width = 1160
    # old_height = 596
    # scale_w = new_width / old_width
    # scale_h = new_height / old_height
    capturedImage = capturedImage._PhotoImage__photo.zoom(2)
    capturedImage = capturedImage.subsample(3)

    image_6 = canvas.create_image(
        605.0,
        329.0,
        image=capturedImage
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("frame7/image_7.png"))

    image_7 = canvas.create_image(
        947.0,
        524.5,
        image=image_image_7
    )

    # button_image_10 = PhotoImage(
    #     file=relative_to_assets("frame7/button_10.png"))
    # button_10 = Button(
    #     image=button_image_10,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_10 clicked"),
    #     relief="flat"
    # )
    # button_10.place(
    #     x=931.0,
    #     y=508.5,
    #     width=31.0,
    #     height=31.0
    # )

    canvas.create_text(
        1128.0,
        532.0,
        anchor="nw",
        text="OMA Perforasi",
        fill="#404040",
        font=("Nunito Regular", 12 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("frame7/image_8.png"))
    image_8 = canvas.create_image(
        1106.0,
        543.5,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("frame7/image_9.png"))
    image_9 = canvas.create_image(
        1106.0,
        511.5,
        image=image_image_9
    )

    canvas.create_text(
        1128.0,
        500.0,
        anchor="nw",
        text="OMA Perforasi",
        fill="#404040",
        font=("Nunito Regular", 12 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("frame7/image_10.png"))
    image_10 = canvas.create_image(
        1106.0,
        479.5,
        image=image_image_10
    )

    canvas.create_text(
        1128.0,
        468.0,
        anchor="nw",
        text="OMA Perforasi",
        fill="#404040",
        font=("Nunito Regular", 12 * -1)
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("frame7/image_11.png"))
    image_11 = canvas.create_image(
        1245.05078125,
        278.0,
        image=image_image_11
    )

    canvas.create_text(
        1082.0,
        92.0,
        anchor="nw",
        text="Analisa Gambar:",
        fill="#404040",
        font=("Nunito Bold", 24 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


switchPage(page=home_page)