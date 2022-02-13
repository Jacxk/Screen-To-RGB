from signal import SIGINT, SIGTERM, signal
from src.interface.mode import available_modes
from src.util import initialize_modes, initialize_sdks


def on_exit(*args):
    print('\nShutting down program.')
    for mode in available_modes:
        mode.disable()
    pass

signal(SIGINT, on_exit)
signal(SIGTERM, on_exit)
    

if __name__ == '__main__':
    print("Program initiated!")
    sdks = initialize_sdks()
    
    sdk_list = []
    
    for SDK in sdks:
        sdk = SDK()
        if not sdk.available():
            continue
        
        sdk_list.append(sdk)
        
    modes = [mode(sdks=sdk_list) for mode in initialize_modes()]
    for mode in modes:
        if 'Screen' in mode.name:
            mode.start()
        
