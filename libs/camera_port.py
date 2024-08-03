import threading
import cv2

def find_camera():
    vidCap_list = []
    cam_index_list = []
    threads = []

    for cam_index in range(20):
        t = threading.Thread(target=try_open_camera, args=(cam_index, vidCap_list, cam_index_list))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if not cam_index_list:
        print("No camera found.")
        return None
    else:
        print("Camera found and opened successfully.")
        return cam_index_list[0]


def try_open_camera(cam_index, vidCap_list, cam_index_list):
    vidCap = cv2.VideoCapture(cam_index)
    if vidCap.isOpened():
        cam_index_list.append(cam_index)
        vidCap.release()
    else:
        print(f"Failed to open camera at index {cam_index}")