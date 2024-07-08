import GPS
from config import GPS_PORT_ADDR

from geopy.distance import geodesic

def on_update_fn(latitude, longitude, speedkm):
    print("Latitude: {},\nLongitute: {}\n".format(latitude, longitude, speedkm))

    origin = (-latitude, longitude)  # (latitude, longitude) don't confuse
    dist = (-8.587058, 116.093217) # rektorat unram

    print("Jarak:")
    print(geodesic(origin, dist).meters, "meter")  # 23576.805481751613
    print(geodesic(origin, dist).kilometers, "km")  # 23.576805481751613
    print(geodesic(origin, dist).miles, "miles")  # 14.64994773134371


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