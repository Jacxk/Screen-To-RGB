from src.interface.mode import available_modes
from src.handlers.modes import screen, keyboard
from src.handlers.sdk.icue import iCue
import signal


def on_exit(*args):
    print('\nShutting down program.')
    for mode in available_modes:
        mode.disable()
    pass

signal.signal(signal.SIGINT, on_exit)
signal.signal(signal.SIGTERM, on_exit)
    

if __name__ == '__main__':
    print("Program initiated!")
    icue_sdk = iCue()

    sdks = [icue_sdk]

    if icue_sdk.available():
        screen_mode = screen.ScreenReact(sdks=sdks)
        #keyboard = keyboard.KeyboardPress(sdks=sdks)
        #sound = sound.SoundReact(sdks=sdks)
        # sound.start()
        # keyboard.start()
        screen_mode.start()
