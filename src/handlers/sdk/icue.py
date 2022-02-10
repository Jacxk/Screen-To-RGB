from src.interface.sdk import SDK
from cuesdk import CueSdk


class iCue(SDK):
    def __init__(self):
        super().__init__("iCue")
        self.sdk = CueSdk()
        self.devices = {}

    def available(self):
        if self.sdk.connect():
            self.enable()
            return True

        print("Handshake failed: %s" % self.sdk.get_last_error())
        return False

    def enable(self):
        super().enable()

        devices = self.sdk.get_devices()
        print(f"    Devices found: {len(devices)}")
        for device in devices:
            self.devices[device.id] = device
            print(
                f"      ({device.id}) Type: '{str(device.type).split('.')[-1]}'; "
                f"Model: '{device.model}'; "
            )

        return self

    def disable(self):
        super().disable()
        self.sdk.release_control()

    def change_colors(self, rgb=(255, 255, 255)):
        if not self.enabled:
            raise Exception(
                f"Trying to change colors while {self.name} SDK is disabled")
        all_leds = self.get_available_leds()
        for device in range(len(all_leds)):
            leds = all_leds[device]
            for led in leds:
                leds[led] = rgb
            self._set_color(device, leds)

        self.sdk.set_led_colors_flush_buffer()

        pass

    def get_available_leds(self):
        leds = [self.sdk.get_led_positions_by_device_index(
            index) for index in range(len(self.devices))]
        return leds

    def _set_color(self, device, rgb):
        self.sdk.set_led_colors_buffer_by_device_index(device, rgb)
