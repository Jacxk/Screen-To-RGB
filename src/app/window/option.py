from functools import partial
from tkinter import Button, FLAT, Frame, N, W, Label, LEFT, S, E

from ..Enums import Theme

buttons = []


class OptionFrame:
    def __init__(self, master=None, description=None, root=None):
        self.description = description
        self.root = root

        self.frame = Frame(master)
        self.description_label = Label(self.frame, text=self.description)

        self.create()

    def create(self):
        frame = self.frame
        frame.grid(
            column=1,
            row=1,
            sticky=N + W,
            rowspan=3,
        )
        self._create_description()

        self.root.bind("<Configure>",
                       lambda _: self.description_label.configure(wraplength=self.root.winfo_width() / 1.5))
        return self

    def _create_description(self):
        label = self.description_label
        label.grid(column=0, row=0)
        label.configure(
            bg=Theme.PRIMARY.value,
            fg=Theme.TEXT.value,
            font=("Helvetica", 12),
            justify=LEFT
        )
        return self

    def set_description(self, text):
        self.frame.configure(text=text)


class OptionButtonFrame:
    def __init__(self, master):
        self.frame = Frame(master, bg=Theme.PRIMARY.value)
        self._create()

    def _create(self):
        self.frame.grid(
            column=0,
            row=1,
            sticky=N + S + W + E,
            pady=50,
            padx=5,
        )
        return self

    def get_frame(self):
        return self.frame


class OptionButton:
    def __init__(self, master, text, frames: [OptionFrame] = []):
        global buttons
        self.active = False
        self.text = text
        self.frames = frames
        self.id = len(buttons)

        self.button = Button(master, text=text)
        self._create()

    def _create(self):
        global buttons
        button = self.button

        button.grid(column=0, row=self.id)
        button.configure(
            bg=Theme.PRIMARY.value,
            activebackground=Theme.SECONDARY.value,
            activeforeground=Theme.TEXT.value,
            fg=Theme.TEXT.value,
            relief=FLAT,
            bd=0,
            padx=50,
            pady=5,
            font=("Helvetica", 12),
        )
        button.bind("<Button-1>", partial(self._on_click))
        buttons.append(self)
        return self

    def _on_click(self, _):
        if len(self.frames) < self.id + 1:
            pass

        self.show()

    def set_hoverable(self):

        def on_enter(button, _):
            button.configure(bg=Theme.HOVER.value)

        def on_leave(self, _):
            if self.active:
                self.button.configure(bg=Theme.ACTIVE.value)
            else:
                self.button.configure(bg=Theme.PRIMARY.value)

        button = self.button

        button.bind("<Enter>", partial(on_enter, button))
        button.bind("<Leave>", partial(on_leave, self))
        return self

    def set_active(self, active=True):
        for button in buttons:
            button.get_button().configure(bg=Theme.PRIMARY.value)
            button.active = False

        if active:
            self.button.configure(bg=Theme.ACTIVE.value)
        else:
            self.button.configure(bg=Theme.PRIMARY.value)

        self.active = active
        return self

    def show(self):
        for frame in self.frames:
            frame.frame.grid_forget()
        self.frames[self.id].create()
        self.set_active()
        return self

    def get_button(self):
        return self.button
