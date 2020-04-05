available_modes = []


class Mode:
    def __init__(self, name, **kwargs):
        self.name = name
        self.active = False
        self._too_many = False

        self.sdks = kwargs.get("sdks", [])
        self.enabled = kwargs.get("enable", False)
        self.color = kwargs.get("color", (0, 0, 0))

        if self.enabled:
            self.enable()

        available_modes.append(self)
        self.available_modes = available_modes

    def run(self):
        """
        Starts running the RGB mode.
        """
        print(f"Running mode '{self.name}'...")
        for mode in available_modes:
            if mode.active and mode.name is not self.name:
                mode._too_many = True
                mode.disable()
        pass

    def enable(self):
        """
        Enables this mode.
        """
        print(f"Mode '{self.name}' has been enabled")
        self.enabled = True
        self.active = True
        return self

    def disable(self):
        """
        Disables this mode.
        """
        if self._too_many:
            print(f"Mode '{self.name}' has been disabled because there is another mode running.")
        else:
            print(f"Mode '{self.name}' has been disabled")
        self.enabled = False
        self.active = False
        pass

    def get_color(self):
        """
        Get the RGB colors of this mode
        """
        return self.color
