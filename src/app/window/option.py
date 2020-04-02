from functools import partial
from tkinter import Button, FLAT, Frame, N, W, Label, LEFT, S, E, Scrollbar, Canvas

from ..Enums import Theme

buttons = []


def create_button(frame, text, target_frames):
    button = OptionButton(frame, text, target_frames).set_hoverable()
    if len(buttons) == 1:
        button.show()

    return button


class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        background = self.cget('bg')
        self.canvas = canvas = Canvas(self)

        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.configure(bd=0, relief=FLAT)

        self.scrollable_frame = Frame(canvas)
        self.scrollable_frame.configure(bg=background, bd=0, relief=FLAT)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor=N + W)
        canvas.configure(
            yscrollcommand=scrollbar.set,
            bg=background,
            bd=0,
            relief=FLAT,
            highlightthickness=0,
        )

        def set_scroll_grid():
            scrollbar.grid(
                column=0,
                row=0,
                rowspan=999,
                sticky=N + S + E,
            )

        def can_scroll():
            try:
                low, high = scrollbar.get()
                if low <= 0.0 and high >= 1.0 or self.scrollable_frame.winfo_height() < scrollbar.winfo_height():
                    scrollbar.grid_forget()
                    return False
                set_scroll_grid()
                return True
            except:
                scrollbar.grid_forget()
                return False

        def scroll(event):
            if can_scroll():
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _bound_mousewheel(event):
            canvas.bind_all("<MouseWheel>", scroll)

        def _unbound_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")

        canvas.bind('<Configure>', lambda _: can_scroll())
        canvas.bind('<Enter>', _bound_mousewheel)
        canvas.bind('<Leave>', _unbound_mousewheel)

        canvas.grid(
            column=0,
            row=0,
            rowspan=999,
            sticky=N + S + W,
        )

        self.grid_rowconfigure(0, weight=1)


class OptionFrame:
    def __init__(self, master=None, description=None, root=None):
        self.description = description
        self.root = root

        self.frame = Frame(
            master,
            bg=Theme.PRIMARY.value,
            padx=20
        )
        self.description_label = Label(
            self.frame,
            text=self.description,
        )

        self.create()

    def create(self):
        frame = self.frame
        frame.grid(
            column=1,
            row=1,
            sticky=N + W + S + E,
            rowspan=3
        )

        self._create_description()
        self.root.bind("<Configure>", lambda _: self.description_label.configure(
            wraplength=self.frame.winfo_width() - 50
        ))
        return self

    def _create_description(self):
        label = self.description_label
        label.grid(column=0, row=0)
        label.configure(
            font=("Helvetica", 12),
            justify=LEFT,
            bg=self.frame.cget("bg"),
            fg=Theme.TEXT.value,
            wraplength=self.frame.winfo_width() - 50
        )
        return self

    def set_description(self, text):
        self.frame.configure(text=text)


class OptionButtonFrame:
    def __init__(self, master):
        self.frame = ScrollableFrame(master, bg=Theme.MODES.value)
        self.frame.canvas.configure(width=240)
        self._create()

    def _create(self):
        self.frame.grid(
            column=0,
            row=1,
            rowspan=999,
            sticky=N + S + W + E,
        )
        return self

    def get_frame(self):
        return self.frame.scrollable_frame


class OptionButton:
    def __init__(self, master, text, frames: [OptionFrame] = []):
        global buttons
        self.active = False
        self.click_cb = None
        self.text = text
        self.master = master
        self.frames = frames
        self.id = len(buttons)

        self.button = Button(master, text=text, wraplength=145)
        self._create()

    def _create(self):
        global buttons
        button = self.button

        button.grid(column=0, row=self.id + 1, sticky=N + S + E + W)
        button.configure(
            bg=self.master.cget('bg'),
            fg=Theme.TEXT.value,
            activebackground=Theme.FOCUS.value,
            activeforeground=Theme.TEXT.value,
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
        if self.click_cb is not None:
            self.click_cb()

        self.show()

    def on_click(self, func):
        self.click_cb = func
        return self

    def set_hoverable(self):

        def on_enter(button, _):
            button.configure(bg=Theme.HOVER.value)

        def on_leave(self, _):
            if self.active:
                self.button.configure(bg=Theme.ACTIVE.value)
            else:
                self.button.configure(bg=self.master.cget("bg"))

        button = self.button

        button.bind("<Enter>", partial(on_enter, button))
        button.bind("<Leave>", partial(on_leave, self))
        return self

    def set_active(self, active=True):
        for button in buttons:
            button.get_button().configure(bg=self.master.cget("bg"))
            button.active = False

        if active:
            self.button.configure(bg=Theme.ACTIVE.value)

        self.active = active
        return self

    def show(self):
        for frame in self.frames:
            frame.frame.grid_forget()

        self.set_active()
        if self.id + 1 > len(self.frames):
            return self

        self.frames[self.id].create()
        return self

    def get_button(self):
        return self.button
