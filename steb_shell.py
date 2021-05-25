from pynput.keyboard import Key, Controller
import time

def main():
    keyboard = Controller()

    keyboard.press(Key.alt)
    time.sleep(0.3)
    keyboard.press(Key.tab)

    time.sleep(0.5)

    keyboard.release(Key.alt)
    keyboard.release(Key.tab)

    time.sleep(0.5)

    keyboard.type("export TERM=xterm")

    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

    keyboard.type("""/usr/bin/script -qc /bin/bash /dev/null""")

    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

    keyboard.press(Key.ctrl)
    keyboard.press("z")

    time.sleep(0.5)

    keyboard.release(Key.ctrl)
    keyboard.release("z")

    time.sleep(0.3)

    keyboard.type("stty raw -echo")

    time.sleep(0.2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.2)

    keyboard.type('fg')

    time.sleep(0.2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


if __name__ == '__main__':
    main()