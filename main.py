from src.index import *

if __name__ == '__main__':
    global wait_for_change
    while True:
        change_led()
        if wait_for_change is True:
            last_frame = take_screen_shot()
