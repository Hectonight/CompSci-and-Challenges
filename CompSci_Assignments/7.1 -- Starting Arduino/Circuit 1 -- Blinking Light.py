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

while True:
    board.digital[13].write(1)
    time.sleep(1.0)                   # Time that the light is on. You can change this number.
    board.digital[13].write(0)
    time.sleep(1.0)                   # Try changing this number too. You can get the blinks to change.