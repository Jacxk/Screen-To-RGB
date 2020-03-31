## Screen To RGB

Sync your RGB lights with your monitor's color.\
Currently supports `Corsair's iCUE`.\
This program takes over iCUE and disables lighting options there.

### Installation:
* Clone or download this repo.
* Download iCUE's SDK from [CorsairOfficial/cue-sdk](https://github.com/CorsairOfficial/cue-sdk/releases).
    * DLL is located inside `redist/` folder. Get the latest version.
* Install [Python 3](https://www.python.org/downloads/).
* Run `install.sh` to install all the dependencies.
* Edit `config.py` and change `icue_dll_path` to the path of the dll you downloaded.
* Run `start.sh` to start the program.


#### TO-DO:
* RGB Fusion integration.
* Maybe other integrations (but I have no way to test them)