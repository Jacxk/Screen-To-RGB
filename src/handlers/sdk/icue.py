from src.wrappers.cue_sdk import CUESDK, CAM, CorsairLedColor, CLK
from src.wrappers.cue_sdk.exceptions import ServerNotFound
from src.interface.sdk import SDK


class iCue(SDK):
    def __init__(self, dll_path):
        super().__init__("iCue")
        self.sdk = CUESDK(dll_path)
        self.enable()

    def available(self):
        try:
            self.sdk.perform_protocol_handshake()
            return True
        except ServerNotFound:
            return False

    def enable(self):
        super().enable()
        self.sdk.request_control(access_mode=CAM.ExclusiveLightingControl)
        return self

    def disable(self):
        super().disable()
        self.sdk.release_control()

    def change_colors(self, rgb=(255, 255, 255)):
        if not self.enabled:
            raise Exception(f"Trying to change colors while {self.name} SDK is disabled")

        sdk = self.sdk
        color = CorsairLedColor(CLK.CLM_1, *rgb)

        sdk.set_led_colors(color)
        pass
