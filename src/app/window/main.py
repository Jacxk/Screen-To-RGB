from .option import OptionButton, OptionButtonFrame, OptionFrame, buttons


def open_window(master, root):
    mode_frame = OptionButtonFrame(master)

    option_frames = [
        OptionFrame(
            master,
            "Your RGB lights will adjust according to what you have and your screen.",
            root
        ),
        OptionFrame(
            master,
            "Your RGB lights will change every time you hit a key on your keyboard or mouse.",
            root
        ),
    ]

    OptionButton(
        mode_frame.get_frame(),
        "Screen Reactive",
        option_frames
    ).show().set_hoverable()
    OptionButton(
        mode_frame.get_frame(),
        "Keyboard Input",
        option_frames
    ).set_hoverable()
