from random import randrange
from pynput import keyboard

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)
        self.listener = None

    def _on_press(self, _):
        if self.random:
            self.set_color(
                color=(randrange(0, 255), randrange(0, 255), randrange(0, 255)))

    def run(self):
        # TODO: Custom colors

        if self.listener is not None:
            self.listener.start()

        super().run()

    def enable(self):
        self.listener = keyboard.Listener(on_press=self._on_press)
        super().enable()

    def disable(self):
        if self.listener is not None:
            self.listener.stop()
        super().disable()
