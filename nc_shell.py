import os
from pynput.keyboard import Key, Controller
import time

def main(port):
    keyboard = Controller()
    os.system("terminator -T 'NetCat' -x '/bin/bash'")

    time.sleep(0.2)

    keyboard.type(f"nc -lnvp {port}")

    time.sleep(0.2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


if __name__ == '__main__':
    main()
