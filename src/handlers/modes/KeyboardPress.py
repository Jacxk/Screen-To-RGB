from random import randrange
from time import sleep
from pynput import keyboard

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)
        self.listener = None

    def _on_key(self, _):
        if self.random:
            before_color = [randrange(0,255),randrange(0,255),randrange(0,255)] if self.color is None else self.color
            color = [randrange(0,255),randrange(0,255),randrange(0,255)]
            while before_color[0] != color[0] and before_color[1] != color[1] and before_color[2] != color[2]:
                if before_color[0] > color[0]:
                    color[0]+=1
                if before_color[1] > color[1]:
                    color[1]+=1
                if before_color[2] > color[2]:
                    color[2]+=1
                if before_color[0] < color[0]:
                    color[0]-=1
                if before_color[1] < color[1]:
                    color[1]-=1
                if before_color[2] < color[2]:
                    color[2]<=1
                sleep(1)
                self.set_color(color=(color[0], color[1], color[2]))
                self.color = color

    def run(self):
        if self.listener is not None:
            self.listener.start()

        super().run()

    def enable(self):
        self.listener = keyboard.Listener(on_release=self._on_key)
        super().enable()

    def disable(self):
        if self.listener is not None:
            self.listener.stop()
        super().disable()
