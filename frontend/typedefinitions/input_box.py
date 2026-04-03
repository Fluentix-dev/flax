from .base import *
import customtkinter as ctk

class InputBox(UIElement):
    def __init__(
        self,
        position: Vector2,
        backgroundColor: Color,
        textColor: Color,
        textFont: Font,
        anchor: ElementAlign = ElementAlign.NoAlign,
        useRelativePos: bool = True
    ):
        super().__init__(position, anchor, useRelativePos)
        self.backgroundColor = backgroundColor
        self.textColor = textColor
        self.textFont = textFont
    
    def Draw(self, wd: Window):
        self.component = ctk.CTk