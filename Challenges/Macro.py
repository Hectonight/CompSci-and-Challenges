from pynput.mouse import Button, Controller
import time

mouse = Controller()

macro = False

while True:
    await asyncio.sleep(0.01)
    mouse.click(Button.left, 1)
