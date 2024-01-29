# Basic Python Outgauge Cluster
print("Loading...")
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 4444))

barpsi = 14.50377377337509

while True:
    data = sock.recv(96)
    if not data:
        break

    outsim_pack = struct.unpack("I4sH2c7f2I3f16s16si", data)

    coolant = (
        "Overheating! ⚠️"
        if outsim_pack[8] > 129
        else "Engine Off!"
        if outsim_pack[8] == 0
        else round((outsim_pack[8] * 1.8) + 32, 2)
    )

    oil_temp = (
        "Engine Off!"
        if outsim_pack[11] == 0
        else round((outsim_pack[11] * 1.8) + 32, 2)
    )

    boost = (
        "No Boost, "
        if outsim_pack[7] == 0
        else f"Boost: {round(outsim_pack[7] * barpsi, 1)} psi, "
    )

    print(
        f"Speed: {round(outsim_pack[5] * 2.237, 1)} mph, "
        f"RPM: {round(outsim_pack[6])}, "
        f"{boost}"
        f"Engine Temperature (°F): {coolant}, "
        f"Fuel: {round(outsim_pack[9] * 100, 1)}%, "
        f"Oil Temperature (°F): {oil_temp}, ",
        f"Throttle: {round(outsim_pack[14] * 100, 1)} %, "
        f"Brake: {round(outsim_pack[15] * 100, 1)} %, "
        f"Clutch: {round(outsim_pack[16] * 100, 1)} % ",
        end="\r",
        flush=True,
    )


sock.close()
