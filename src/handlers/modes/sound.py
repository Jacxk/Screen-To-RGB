from src.interface.mode import Mode
import sounddevice as sd
import numpy as np


class SoundReact(Mode):
    def __init__(self, **kwargs):
        super().__init__("Sound Reactive", **kwargs)

    # TODO: Finish this implementation
    def run(self):
        super().run()

        def print_sound(indata, frames, time, status):
            volume_norm = np.linalg.norm(indata) * 10
            print("|" * int(volume_norm))

        with sd.InputStream(callback=print_sound):
            sd.sleep(10000)

    def disable(self):
        super().disable()
