from random import randrange
from time import sleep
from pynput import keyboard
from ...color import fade_between

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)
        self.listener = None
        self.color = [0, 0, 0]

    def _on_key(self, key):
        self.pressed_key = key
        if self.random:
            [self.set_color(color=c) for c in fade_between(self.color)]

    def run(self):
        if self.listener is not None:
            self.listener.start()

        super().run()

    def enable(self):
        self.listener = keyboard.Listener(on_press=self._on_key)
        super().enable()

    def disable(self):
        if self.listener is not None:
            self.listener.stop()
        super().disable()
