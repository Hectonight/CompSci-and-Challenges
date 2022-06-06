from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

board = pyfirmata.Arduino(port)
iterator = pyfirmata.util.Iterator(board)
iterator.start()

a0: pyfirmata.Pin = board.get_pin("a:0:i")
d3: pyfirmata.Pin = board.get_pin("d:3:o")
d4: pyfirmata.Pin = board.get_pin("d:4:o")

while True:
    pos = a0.read()
    if pos is not None:
        if pos <= 1/3:
            d3.write(False)
            d4.write(False)
        elif pos <= 2/3:
            d3.write(True)
            d4.write(False)
        else:
            d3.write(True)
            d4.write(True)
        time.sleep(0.1)




