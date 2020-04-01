from tkinter import Frame, Button, Label, Listbox, StringVar


class Window(Frame):
    def __init__(self, master=None, conf=None, **kw):
        if conf is None:
            conf = {}
        Frame.__init__(self, master, conf, **kw)
        self.master = master
        self.exitButton = None
        self.label = None
        self.list = None
        self.i = 0

        self.create_button()
        self.create_label()
        self.create_list_box()

    def create_button(self):
        self.exitButton = Button(
            master=self.master,
            text="Exit",
            command=exit
        )
        self.exitButton.place(x=0, y=0)

    def create_label(self):
        self.label = Label(
            master=self.master,
            text=self.i,
            fg="Red"
        )
        self.label.place(x=50, y=50)
        self.increment()

    def create_list_box(self):
        items = StringVar()
        items.set(("React with screen", "Change with keys"))

        list = Listbox(
            master=self.master,
            listvariable=items
        )
        list.pack()
        list.bind("<<ListboxSelect>>", lambda _: print(list.curselection()[0]))

        self.list = list

    def increment(self):
        self.i += 1
        self.label.configure(text=self.i)
        self.after(1000, self.increment)
