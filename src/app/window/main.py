from tkinter import Label, NSEW

from .option import OptionButton, OptionButtonFrame, OptionFrame, create_button, ScrollableFrame
from ..Enums import Theme


def open_window(master, root):
    mode_frame = OptionButtonFrame(master)

    option_frames = [
        OptionFrame(
            master,
            "Your RGB lights will adjust according to what you have and your screen."+
            "Your RGB lights will adjust according to what you have and your screen."+
            "Your RGB lights will adjust according to what you have and your screen."+
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

    create_button(mode_frame.get_frame(), "Screen Reactive", option_frames)
    create_button(mode_frame.get_frame(), "Keyboard Input", option_frames)

