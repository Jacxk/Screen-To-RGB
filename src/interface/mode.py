class Mode:
    def __init__(self, name, **kwargs):
        self.name = name
        self.available = True
        self.sdks = kwargs.get("sdks", [])
        self.enabled = kwargs.get("enable", False)
        self.color = kwargs.get("color", (0, 0, 0))
        self.enable()

    def run(self):
        """
        Starts running the RGB mode.
        """
        pass

    def enable(self):
        """
        Enables this mode.
        """
        print(f"Mode '{self.name}' has been enabled")
        self.enabled = True
        pass

    def disable(self):
        """
        Disables this mode.
        """
        print(f"Mode '{self.name}' has been disabled")
        self.enabled = False
        pass

    def get_color(self):
        """
        Get the RGB colors of this mode
        """
        return self.color
