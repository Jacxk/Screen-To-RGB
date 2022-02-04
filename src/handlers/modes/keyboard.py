from random import randrange

import keyboard

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)

    def run(self):
        def _callback(_):
            if self.random:
                self.set_color((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            # TODO: Custom colors

        keyboard.on_press(_callback)

        super().run()

    def disable(self):
        keyboard.unhook_all()
        super().disable()
