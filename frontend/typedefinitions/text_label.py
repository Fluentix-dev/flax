from .base import *
from .window import *
from customtkinter import CTkLabel


class TextLabel(UIElement):
    """
    A text label
    """
    def __init__(
            self,
            position: Vector2 = Vector2(0, 0),
            useRelativePos: bool = True,
            data: str = "",
            font: Font = Font("Hello Fluentix", 14),
            anchor: ElementAlign = ElementAlign.NoAlign,
            backgroundColor: Color | None = None,
            textColor: Color = Color(0, 0, 0),
        ):

        super().__init__(position, anchor, useRelativePos)
        self.data = data
        self.font = font
        self.anchor = anchor
        self.backgroundColor = backgroundColor
        self.textColor = textColor
        self.useRelativePos = useRelativePos
    
    def Draw(self, wd: Window):
        """
        Draws the label onto the screen
        """

        label = CTkLabel(
            wd.wd,
            text=self.data,
            text_color=self.textColor.ToHex(),
            font=self.font.GetFont(),
            fg_color=self.backgroundColor.ToHex() if self.backgroundColor else "transparent",
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

        label.place(**place_args)