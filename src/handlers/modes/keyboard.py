from random import randrange
from pynput import keyboard

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)

    def run(self):
        def _on_press(_):
            if self.random:
                self.set_color(
                    color=(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            # TODO: Custom colors

        listener = keyboard.Listener(on_press=_on_press)
        listener.start()

        super().run()

    def disable(self):
        keyboard.unhook_all()
        super().disable()
