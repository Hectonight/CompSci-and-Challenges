from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

# The right string input here might be different on your computer.
# Once the Arduino is plugged into your computer, go to
# the Arduino IDE, then do:
# Tools > Port and find the Port that is similar to the one
# below (NOT Bluetooth). The numbers on the end might be different.
# Change the input below so that it matches whatever you see
# in the Arduino IDE.


board = pyfirmata.Arduino(port)

iterator = pyfirmata.util.Iterator(board)
iterator.start()

board.digital[10].mode = pyfirmata.INPUT


speed1 = None
speed2 = 1.0
speed3 = 0.25

modes = [speed1, speed2, speed3]
mode = 0

input10Old = False

while True:

	input10New = board.digital[10].read()

	if input10New is None:
		input10New = False

	if (not input10Old) and input10New:
		mode += 1 if mode < 2 else -2


	input10Old = input10New

	if input10Old is None:
		input10Old = False

	if modes[mode] is None:
		board.digital[13].write(1)
	else:
		board.digital[13].write(1)
		time.sleep(modes[mode])
		board.digital[13].write(0)
		time.sleep(modes[mode])