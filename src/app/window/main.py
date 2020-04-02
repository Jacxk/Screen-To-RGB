from tkinter import Label, NSEW

from .option import OptionButtonFrame, OptionFrame, create_button
from ..Enums import Theme
from ...index import change_led

loop_functions = {}


def add_to_loop(func):
    loop_functions[func.__name__] = func


def create_app(master, root):
    mode_frame = OptionButtonFrame(master)

    option_frames = [
        OptionFrame(
            master,
            "Your RGB lights will adjust according to what you have and your screen."
            ,
            root
        ),
        OptionFrame(
            master,
            "Your RGB lights will change every time you hit a key on your keyboard or mouse.",
            root
        ),
    ]

    mode_label = Label(master, text="RGB Mode")
    mode_label.configure(
        font=("Helvetica", 12),
        pady=40,
        bg=Theme.SECONDARY.value,
        fg=Theme.TEXT.value,
    )
    mode_label.grid(
        column=0,
        row=0,
        sticky=NSEW,
    )

    create_button(
        mode_frame.get_frame(),
        "Screen Reactive",
        option_frames,
    ).on_click(lambda: add_to_loop(change_led))
    create_button(
        mode_frame.get_frame(),
        "Keyboard Input",
        option_frames,
    ).on_click(lambda: print("Coming Soon!"))

    def start_loop(time=20):
        def task():
            for name in loop_functions:
                loop_functions[name]()
            root.after(time, task)

        root.after(time, task)

    start_loop()
