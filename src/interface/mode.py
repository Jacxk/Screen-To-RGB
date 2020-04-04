class Mode:
    def __init__(self, name, **kwargs):
        self.name = name
        self.available = True
        self.enabled = kwargs.get("enable", False)
        self.color = kwargs.get("color", (0, 0, 0))

    def run(self, *sdks):
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
        pass
