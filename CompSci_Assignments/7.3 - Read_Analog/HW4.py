from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

board = pyfirmata.Arduino(port)
iterator = pyfirmata.util.Iterator(board)
iterator.start()

a0: pyfirmata.Pin = board.get_pin("a:0:i")
d3: pyfirmata.Pin = board.get_pin("d:3:o")

halfTurn = False

while True:
    pos = a0.read()
    if pos is not None:
        if pos > 0.5:
            halfTurn = True
        elif halfTurn:
            d3.write(not d3.read())
            halfTurn = False
    time.sleep(0.1)