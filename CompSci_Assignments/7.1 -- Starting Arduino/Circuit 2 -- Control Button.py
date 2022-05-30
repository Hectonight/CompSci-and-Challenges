from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

# Again, you might need to change the input here.
# Should be the same as whatever worked in Demo 1.
board = pyfirmata.Arduino(port)

# An iterator is a loop that runs "in parallel" with your
# main code. This loop checks the input from the button.
iterator = pyfirmata.util.Iterator(board)
iterator.start()

board.digital[10].mode = pyfirmata.INPUT

while True:
	button_input = board.digital[10].read()
	if button_input:
		board.digital[13].write(1)
	else:
		board.digital[13].write(0)
	time.sleep(0.1)
