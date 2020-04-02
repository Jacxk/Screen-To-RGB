from tkinter import Tk, N, Label, Frame

from .Enums import Theme
from .window.main import open_window

root = Tk()


def start():
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

    open_window(content, root)

    content.columnconfigure(1, weight=1)
    content.rowconfigure(1, weight=1)


def init():
    root.wm_title("Screen to RGB")
    root.geometry("1000x500")
    root.wm_minsize(920, 500)
    start()
    root.mainloop()
