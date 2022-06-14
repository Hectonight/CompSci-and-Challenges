from CompSci_Assignments.portDetermine import port
import pyfirmata
import time

board = pyfirmata.Arduino(port)  # Change to a different port if necessary.
iterator = pyfirmata.util.Iterator(board)
iterator.start()

a0: pyfirmata.Pin = board.get_pin("a:0:i")
a1: pyfirmata.Pin = board.get_pin("a:1:i")
d3: pyfirmata.Pin = board.get_pin("d:3:o")
d4: pyfirmata.Pin = board.get_pin("d:4:o")

while True:
    sound = a0.read()
    light = a1.read()

    if None not in [sound, light]:
        someone_there = sound > 0.6
        lights_on = light > 0.3

        alert = someone_there and not lights_on

        d3.write(alert)
        d4.write(not (someone_there or lights_on))

        time.sleep(5 * alert)


    time.sleep(0.1)