import GPS
from config import GPS_PORT_ADDR

def on_update_fn(latitude, longitude, speedkm):
    print("Latitude: {},\nLongitute: {}\nSpeed (Km) is {}\n\n".format(latitude, longitude, speedkm))

def on_error_fn(msg):
    print("Error is {}".format(msg))


GPS.on_update = on_update_fn
GPS.on_error = on_error_fn


def main():
    open = GPS.begin(port=GPS_PORT_ADDR)

    while True:
        GPS.loop(open)

if __name__ == '__main__':
    main()