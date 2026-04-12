from .base import *
import customtkinter as ctk

class InputBox(UIElement):
    def __init__(
        self,
        position: Vector2 = Vector2(0, 0),
        size: Vector2Int = Vector2Int(0, 0),
        backgroundColor: Color = Color(0, 0, 0),
        textColor: Color = Color(255, 255, 255),
        textFont: Font = Font("Hello Fluentix!", 14),
        hidden: bool = False,
        placeholderText: str = "",
        placeholderColor: Color = Color(128, 128, 128),
        anchor: ElementAlign = ElementAlign.NoAlign,
        useRelativePos: bool = True
    ):
        super().__init__(position, anchor, useRelativePos)
        self.size = size
        self.backgroundColor = backgroundColor
        self.textColor = textColor
        self.textFont = textFont
        self.hidden = hidden
        self.placeholderText = placeholderText
        self.placeholderColor = placeholderColor

    def Draw(self, wd: Window):
        if self.hidden:
            self.component = ctk.CTkEntry(
                wd.wd,
                font=self.textFont.GetFont(),
                fg_color=self.backgroundColor.ToHex(),
                text_color=self.textColor.ToHex(),
                placeholder_text=self.placeholderText,
                placeholder_text_color=self.placeholderColor.ToHex(),
                width=self.size.x,
                height=self.size.y,
                show="*"
            )
        else:
            self.component = ctk.CTkEntry(
                wd.wd,
                font=self.textFont.GetFont(),
                fg_color=self.backgroundColor.ToHex(),
                text_color=self.textColor.ToHex(),
                placeholder_text=self.placeholderText,
                placeholder_text_color=self.placeholderColor.ToHex(),
                width=self.size.x,
                height=self.size.y
            )
        
        place_args = {}
    
        if self.useRelativePos:
            place_args["relx"] = self.position.x / wd.width
            place_args["rely"] = self.position.y / wd.height
        else:
            place_args["x"] = self.position.x
            place_args["y"] = self.position.y


        if self.anchor != ElementAlign.NoAlign:
            place_args["anchor"] = self.anchor.value
        else:
            place_args["anchor"] = 'center'

        self.component.place(**place_args)
    
    def getInput(self):
        try:
            return self.component.get()
        except Exception:
            return ""