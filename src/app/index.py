from functools import partial
from tkinter import Tk, N, S, E, W, Button, Label, Frame

root = Tk()


def test():
    content = Frame(root, bg="#202020", width=100, height=100)
    content.pack(fill="both", expand=True)

    title = Label(content, text="Screen To RGB")
    title.configure(bg="#202020", fg="white", font=("Helvetica", 30))
    title.grid(
        column=0,
        row=0,
        columnspan=2,
        pady=10,
        sticky=N,
    )

    mode = Frame(content)
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
    )

    desc = [
        "Your RGB lights will adjust according to what you have and your screen.",
        "Your RGB lights will change every time you hit a key on your keyboard or mouse."
    ]

    label = Label(option, text=desc[0])
    label.grid(column=0, row=0)
    label.configure(bg="#202020", fg="white", font=("Helvetica", 16))

    root.bind("<Configure>", lambda _: label.configure(wraplength=root.winfo_width()/1.5))

    buttons = [
        Button(mode, text="Screen Reactive"),
        Button(mode, text="Keyboard Input")
    ]

    for i, button in enumerate(buttons):
        button.grid(column=0, row=i)
        button.configure(bg="#202020", fg="white")
        button.bind("<Button-1>", partial(lambda p, e: label.configure(text=desc[p]), i))

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
