import numpy as np
from PIL import Image
from mss import mss
from scipy import cluster

from src.interface.mode import Mode


class ScreenReact(Mode):
    def __init__(self, **kwargs):
        super().__init__("Screen Reactive", **kwargs)

    def _exec(self):
        self.set_color(color=self.get_dominant_color())
        pass

    def get_screen(self):
        with mss() as sct:
            sct_img = sct.grab(sct.monitors[0])

            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            img = img.resize((100, 100))
            return img

    def get_dominant_color(self):
        img_array = np.asarray(self.get_screen())
        shape = img_array.shape
        img_array = img_array.reshape(np.product(shape[:2]), shape[2]).astype(float)

        codes, _ = cluster.vq.kmeans(img_array, 1)
        self.color = list(map(int, codes[0]))
        return self.color
