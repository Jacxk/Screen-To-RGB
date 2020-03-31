import time
import numpy as np
import scipy.cluster

from PIL import Image, ImageChops
from mss import mss

from .cue_sdk import *
from .config import *

last_frame = None

Corsair = CUESDK(icue_dll_path)
in_control = Corsair.RequestControl(CAM.ExclusiveLightingControl)

if in_control is False:
    print("There was an error while requesting control of the SDK")
    exit(1)

current_led = [0] * 3


def take_screen_shot():
    with mss() as sct:
        sct_img = sct.grab(sct.monitors[screen])

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        img = img.resize((1, 1))
        return img


def change_led():
    global current_led, last_frame, wait_for_change, smooth
    img = take_screen_shot()

    if wait_for_change is True and last_frame is not None:
        diff = ImageChops.difference(img, last_frame)
        bbox = diff.getbbox()
        if bbox is None:
            return

    img_array = np.asarray(img)
    shape = img_array.shape
    img_array = img_array.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, _ = scipy.cluster.vq.kmeans(img_array, 1)
    codes = list(map(int, codes[0]))

    if smooth is False:
        Corsair.set_led_colors(CorsairLedColor(CLK.CLM_1, *codes))
        return

    height, width = 2, 4
    r1, g1, b1 = current_led
    r2, g2, b2 = codes

    for y in range(int(height / 2)):
        for x in range(width):
            p = x / float(width - 1)
            r = int((1.0 - p) * r1 + p * r2 + 0.5)
            g = int((1.0 - p) * g1 + p * g2 + 0.5)
            b = int((1.0 - p) * b1 + p * b2 + 0.5)
            for i in range(1, 155):
                Corsair.set_led_colors(CorsairLedColor(CLK.CLM_1, *(r, g, b)))
            time.sleep(0.02)

    current_led = codes
