from customtkinter import CTk, set_appearance_mode
from enum import Enum

class WindowAppearanceMode(Enum):
    Light = "light"
    Dark = "dark"

class Window:
    """
    Defines a window for the app
    """
    def __init__(self, width: int, height: int, appearanceMode: WindowAppearanceMode = WindowAppearanceMode.Light, title: str = "Hello Fluentix!"):
        self.width = width
        self.height = height
        self.wd = CTk()
        self.wd.geometry(f"{self.width}x{self.height}")
        set_appearance_mode(appearanceMode.value)
        self.wd.title(title)

    def Run(self):
        """
        Runs the window
        """
        self.wd.mainloop()