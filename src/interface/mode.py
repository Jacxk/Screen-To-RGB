from threading import Thread

available_modes = []


class Mode:
    def __init__(self, name, **kwargs):
        self.name = name
        self.active = False
        self._too_many = False
        self.running_thread = None

        self.sdks = kwargs.get("sdks", [])
        self.enabled = kwargs.get("enable", True)
        self.color = kwargs.get("color", None)
        
        print(f"Enabling {self.name}.")

        if self.enabled:
            self.enable()

        available_modes.append(self)
        self.available_modes = available_modes

    def start(self):
        if self.running_thread is None:
            self.running_thread = Thread(
                name=self.name, target=self.run)
            self.running_thread.start()

    def run(self):
        """
        Starts running the RGB mode.
        """
        print(f"    Running mode '{self.name}'...")
        for mode in available_modes:
            if mode.enabled and mode.active and mode.name is not self.name:
                mode._too_many = True
                mode.disable()

        while self.enabled and self.active:
            self._exec()

    def _exec(self):
        """
        Mode's execution logic.
        """

    def enable(self):
        """
        Enables this mode.
        """
        print(f"    Mode '{self.name}' has been enabled")
        self.enabled = True
        self.active = True
        return self

    def disable(self):
        """
        Disables this mode.
        """
        if self._too_many:
            print(
                f"Mode '{self.name}' has been disabled because there is another mode running.")
        else:
            print(f"Mode '{self.name}' has been disabled")
        self.enabled = False
        self.active = False
        self._too_many = False

    def get_color(self):
        """
        Get the RGB colors of this mode
        """
        return self.color

    def set_color(self, **kwargs):
        """
        Set the RGB colors to be displayed with the SDKs
        """
        self.color = kwargs.get("color")
        for sdk in self.sdks:
            if sdk.enabled:
                sdk.change_colors(self.get_color())
        return self
