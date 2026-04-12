from .base import *
from .window import Window
import customtkinter as ctk
from types import FunctionType

class Button(UIElement):
    def __init__(
        self,
        position: Vector2,
        buttonSize: Vector2Int,
        color: Color,
        hoverColor: Color,
        activationFunction: FunctionType,
        anchor: ElementAlign = ElementAlign.NoAlign,
        useRelativePos: bool = True,
        textLabel: str = "",
        textLabelColor: Color = Color(0,0,0),
        textLabelFont: Font = Font("Fluentix", 20)
    ):
        super().__init__(position, anchor, useRelativePos)
        self.buttonSize = buttonSize
        self.color = color
        self.hoverColor = hoverColor
        self.textLabel = textLabel
        self.textLabelColor = textLabelColor
        self.textLabelFont = textLabelFont
        self.activationFunction = activationFunction
    
    def Draw(self, wd: Window):
        button = ctk.CTkButton(wd.wd, command=self.activationFunction, fg_color=self.color.ToHex(), hover_color=self.hoverColor.ToHex(), width=self.buttonSize.x, height=self.buttonSize.y, text=self.textLabel, text_color=self.textLabelColor.ToHex(), font=self.textLabelFont.GetFont())
        button.place(relx=self.position.x / wd.width, rely=self.position.y / wd.height)

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

        button.place(**place_args)