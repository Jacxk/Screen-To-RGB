from src.config import icue_dll_path
from src.handlers.modes.keyboard import KeyboardPress
from src.handlers.modes.screen import ScreenReact
from src.handlers.modes.sound import SoundReact
from src.handlers.sdk.icue import iCue

if __name__ == '__main__':
    print("Program initiated!")
    icue_sdk = iCue(icue_dll_path)

    if icue_sdk.available():
        #screen_mode = ScreenReact(sdks=[icue_sdk])
        #keyboard = KeyboardPress(sdks=[icue_sdk])
        sound = SoundReact(sdks=[icue_sdk])
        sound.start()
        #keyboard.start()
        #screen_mode.start()
