from random import randrange

import keyboard

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)

    def run(self):
        super().run()

        def callback(_):
            for sdk in self.sdks:
                if not sdk.enabled:
                    return
                if self.random:
                    sdk.change_colors((randrange(0, 255), randrange(0, 255), randrange(0, 255)))

        keyboard.on_press(callback)
        keyboard.wait()

    def disable(self):
        keyboard.unhook_all()
        super().disable()
