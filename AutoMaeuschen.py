import pyautogui
import random
import time
import ctypes


def do_random_thing():
    did_something = False
    if random.random() > 0.99:
        pyautogui.click()
        print('clickity click')
        did_something = True
    if random.random() > 0.92:
        pyautogui.scroll(random.randint(-10, 10))
        print('scrollity scroll')
    if random.random() > 0.99:
        pyautogui.press('esc')
        print('oooh nooo, ESCAPE!!!')
        did_something = True

    if did_something:
        time.sleep(5)


def random_walk():
    a, b = pyautogui.position()
    a_size, b_size = pyautogui.size()
    max_a = int(0.8*a_size)
    min_a = int(0.2*a_size)
    max_b = int(0.8*b_size)
    min_b = int(0.2*b_size)
    while 1:
        a += random.randint(-50, 50)
        a = max([min_a, min([max_a, a])])
        b += random.randint(-40, 40)
        b = max([min_b, min([max_b, b])])
        pyautogui.moveTo(a, b, duration=0.001)
        do_random_thing()


if __name__ == '__main__':
    try:
        # prevent Sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
        random_walk()
    except KeyboardInterrupt:
        # set back to normal
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        print('Script terminated')
