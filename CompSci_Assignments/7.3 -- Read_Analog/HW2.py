from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

board = pyfirmata.Arduino(port)
iterator = pyfirmata.util.Iterator(board)
iterator.start()

a0: pyfirmata.Pin = board.get_pin("a:0:i")
d3: pyfirmata.Pin = board.get_pin("d:3:o")


while True:
    timer = a0.read()
    if timer is not None:
        time.sleep(timer)
        d3.write(True)
        time.sleep(timer)
        d3.write(False)
