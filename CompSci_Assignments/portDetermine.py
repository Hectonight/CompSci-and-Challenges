from sys import platform

winPort = "COM3"
macOSPort = "/dev/cu.usbmodem14101"


if platform == "win32":
	port = winPort
elif platform == "darwin":
	port = macOSPort
else:
	raise Exception("Cannot determine Port")