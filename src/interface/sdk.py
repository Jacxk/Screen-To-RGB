from src.interface.mode import Mode


class SDK:
    def __init__(self, name):
        self.name = name
        self.enabled = False

    def available(self):
        """
        Checks if the current SDK is available for use.
        """
        pass

    def enable(self):
        """
        Enables this SDK.
        """
        print(f"SDK '{self.name}' has been enabled")
        self.enabled = True
        pass

    def disable(self):
        """
        Disables this SDK.
        """
        print(f"SDK '{self.name}' has been disabled")
        self.enabled = False
        pass

    def change_colors(self, rgb):
        """
        Change lights' colors.
        """
        pass

    def enable_mode(self, mode: Mode):
        """
        Enable mode on this SDK
        :param mode:
        """
        pass
