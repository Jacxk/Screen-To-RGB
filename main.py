from src.handlers.modes import screen, keyboard, sound
from src.handlers.sdk.icue import iCue

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

    while True:
        pass
