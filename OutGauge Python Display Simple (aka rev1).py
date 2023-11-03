print(
    "Welcome to LS's Basic Python Outgauge Cluster, a project that has evolved significantly from its humble origins. Originally inspired by a simpler program crafted by angelo234 on the BeamNG.drive forums, it has undergone numerous enhancements and modifications, making it uniquely my own creation. Should you encounter prolonged loading times or encounter data retrieval issues, I kindly request that you verify the accuracy of your settings and ensure that the game is correctly launched with a loaded vehicle."
)

import socket
import struct

print("Loading...")
# Create UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to BeamNG OutGauge.
sock.bind(("127.0.0.1", 4444))

barpsi = 14.50377377337509  # had to use a very precise conversion, else the figure would be off my a few hundredths of a psi


while True:
	# Receive data.
	data = sock.recv(96)


	if not data:
		break # Lost connection

	# Unpack the data.
	outsim_pack = struct.unpack('I4sH2c7f2I3f16s16si', data)
	
	print("Fuel: %",
        str((((outsim_pack[9] * 100)))),
        "Speed: ",
        str((round((outsim_pack[5] * 2.237), 1))),
        "RPM: ",
        str((round((outsim_pack[6]), 1))),
        "Engine Temperature: ",
        str((round(((outsim_pack[8] * 1.8) + 32), 1))),
        "Turbo Pressure: ",
        str((round((outsim_pack[7] * barpsi), 1))),
        end="\r",
        flush=True,
    ) 
	
# Release the socket.
sock.close()
