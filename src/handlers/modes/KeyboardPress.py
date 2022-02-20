from random import randrange
from threading import Thread
from queue import Queue
from pynput import keyboard
from ...color import fade_between

from src.interface.mode import Mode


class KeyboardPress(Mode):
    def __init__(self, **kwargs):
        super().__init__("Keyboard Press", **kwargs)
        self.random = kwargs.get("random", True)
        self.listener = None
        self.color = [0, 0, 0]
        self.input_thread = None
        self.queue = Queue()

    def _on_key(self, key):
        if self.random:
            self.queue.put(key)
            if not self.input_thread:
                self.input_thread = Thread(name=self.name, target=self._change_color, daemon=True)
                self.input_thread.start() 


    def start(self):
        return super().start()

    def run(self):
        if self.listener is not None:
            self.listener.start()
        super().run()

    def _change_color(self):
        while not self.queue.empty():
            for _ in range(self.queue.qsize()):
                self.queue.get()
                self.queue.task_done()
            
            for c in fade_between(self.color):
                self.set_color(color=c)
        self.input_thread = None 

    def enable(self):
        self.listener = keyboard.Listener(on_release=self._on_key)
        super().enable()

    def disable(self):
        if self.listener is not None:
            self.listener.stop()
        super().disable()
