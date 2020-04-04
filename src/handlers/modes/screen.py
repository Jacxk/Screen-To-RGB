from PIL import Image
from mss import mss
import numpy as np
from scipy import cluster

from src.interface.mode import Mode
from src.interface.sdk import SDK


class ScreenReact(Mode):
    def __init__(self, **kwargs):
        super().__init__("Screen Reactive", **kwargs)
        self.enable()

    def run(self, *sdks: SDK):
        while self.enabled:
            for sdk in sdks:
                if not sdk.enabled:
                    return
                sdk.change_colors(self.get_dominant_color())
        pass

    def get_screen(self):
        with mss() as sct:
            sct_img = sct.grab(sct.monitors[0])

            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            img = img.resize((1, 1))
            return img

    def get_dominant_color(self):
        img_array = np.asarray(self.get_screen())
        shape = img_array.shape
        img_array = img_array.reshape(np.product(shape[:2]), shape[2]).astype(float)

        codes, _ = cluster.vq.kmeans(img_array, 1)
        return list(map(int, codes[0]))
