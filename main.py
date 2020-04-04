from src.config import icue_dll_path
from src.handlers.modes.screen import ScreenReact
from src.handlers.sdk.icue import iCue


if __name__ == '__main__':
    print("Program initiated!")
    icue_sdk = iCue(icue_dll_path)
    screen_mode = ScreenReact()
    screen_mode.run(icue_sdk)
