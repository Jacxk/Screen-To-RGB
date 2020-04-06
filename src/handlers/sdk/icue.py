from src.interface.sdk import SDK
from src.wrappers.cue_sdk import CUESDK, CAM, CorsairLedColor, CorsairDeviceInfo, CDT
from src.wrappers.cue_sdk.exceptions import ServerNotFound


class iCue(SDK):
    def __init__(self, dll_path):
        super().__init__("iCue")
        self.sdk = CUESDK(dll_path)
        self.devices = []
        self.enable()

    def available(self):
        try:
            self.sdk.perform_protocol_handshake()
            return True
        except ServerNotFound:
            return False

    def enable(self):
        self.enabled = self.sdk.request_control(access_mode=CAM.ExclusiveLightingControl)
        super().enable()

        count = self.sdk.get_device_count()
        print(f"    Devices found: {count}")
        for i in range(count):
            info = self.sdk.get_device_info(i)
            self.devices.append(info)
            print(
                f"      ({i + 1}) Type: '{info.type.name}'; "
                f"Model: '{info.model}'; "
            )

        return self

    def disable(self):
        super().disable()
        self.sdk.release_control()

    def change_colors(self, rgb=(255, 255, 255)):
        if not self.enabled:
            raise Exception(f"Trying to change colors while {self.name} SDK is disabled")

        for device in self.devices:
            self._set_color(device, rgb)

        pass

    def _set_color(self, device: CorsairDeviceInfo, rgb):
        device_type = device.type
        sdk = self.sdk

        if device_type is CDT.Mouse:
            for i in range(4):
                color = CorsairLedColor(148 + i, *rgb)
                sdk.set_led_colors(color)
        elif device_type is CDT.Keyboard:
            for i in range(147):
                color = CorsairLedColor(i + 1, *rgb)
                sdk.set_led_colors(color)
        elif device_type is CDT.Headset:
            for i in range(2):
                color = CorsairLedColor(152 + i, *rgb)
                sdk.set_led_colors(color)
        elif device_type is CDT.Unknown:
            for i in range(154):
                color = CorsairLedColor(i + 1, *rgb)
                sdk.set_led_colors(color)
