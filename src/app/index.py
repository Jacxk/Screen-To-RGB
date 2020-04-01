from enum import Enum
from functools import partial
from tkinter import Tk, N, S, E, W, Button, Label, Frame, FLAT

root = Tk()


class Theme(Enum):
    PRIMARY = "#202020"
    SECONDARY = "#606060"
    TEXT = "#FFFFFF"
    ACTIVE = "#404040"


def test():
    content = Frame(root, bg="#202020")
    content.pack(fill="both", expand=True)

    title = Label(content, text="Screen To RGB")
    title.configure(bg=Theme.PRIMARY.value, fg="white", font=("Helvetica", 30))
    title.grid(
        column=0,
        row=0,
        columnspan=2,
        pady=10,
        sticky=N,
    )

    mode = Frame(content, bg=Theme.PRIMARY.value)
    mode.grid(
        column=0,
        row=0,
        sticky=N + S + W,
        pady=50,
        padx=50,
        rowspan=2,
    )

    option = Frame(content)
    option.grid(
        column=1,
        row=1,
        sticky=N,
        rowspan=3,
    )

    desc = [
        "Your RGB lights will adjust according to what you have and your screen.",
        "Your RGB lights will change every time you hit a key on your keyboard or mouse."
    ]

    label = Label(option, text=desc[0])
    label.grid(column=0, row=0)
    label.configure(bg=Theme.PRIMARY.value, fg=Theme.TEXT.value, font=("Helvetica", 16))

    root.bind("<Configure>", lambda _: label.configure(wraplength=root.winfo_width() / 1.5))

    buttons_name = [
        "Screen Reactive",
        "Keyboard Input"
    ]

    buttons = []

    def on_click(p, button, _):
        for btn in buttons:
            btn.configure(bg=Theme.PRIMARY.value)

        button.configure(bg=Theme.ACTIVE.value)
        label.configure(text=desc[p])

    for i, btxText in enumerate(buttons_name):
        button = Button(mode, text=btxText)
        button.grid(column=0, row=i)
        button.configure(
            bg=Theme.PRIMARY.value,
            activebackground=Theme.SECONDARY.value,
            activeforeground=Theme.TEXT.value,
            fg=Theme.TEXT.value,
            relief=FLAT,
            bd=0,
            padx=50,
            pady=5
        )

        button.bind("<Button-1>", partial(on_click, i, button))
        buttons.append(button)

    on_click(0, buttons[0], None)

    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=1)
    content.columnconfigure(1, weight=1)
    content.rowconfigure(1, weight=1)


def init():
    root.wm_title("Screen to RGB")
    root.geometry("1000x500")
    root.wm_minsize(920, 500)
    test()
    root.mainloop()
