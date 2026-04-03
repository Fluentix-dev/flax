"""
Script that has the overall classes for frontend UI.
"""
from __future__ import annotations
from enum import IntFlag, Enum
from customtkinter import CTkFont
from .window import Window


class ElementAlign(Enum):
    """
The desired anchor for the element:

[nw]     [n]     [ne]

[w]   [center]   [e]

[sw]     [s]     [se]
    """
    NoAlign = ""
    NorthWest = "nw"
    NorthEast = "ne"
    SouthWest = "sw"
    SouthEast = "se"
    North = "n"
    East = "e"
    South = "s"
    West = "w"
    Center = "center"

class UIElement:
    """
    Base class for UI
    """
    def __init__(self, position: Vector2, anchor: ElementAlign = ElementAlign.NoAlign, useRelativePos: bool = True): # And some attributes
        """
        Attributes shits
        """
        self.position = position
        self.anchor = anchor
        self.useRelativePos = useRelativePos

    def Draw(self, wd: Window):
        """
        Draw
        """


    def Interact(self):
        """
        What do we do when interacting?
        """

    
    def Destroy(self):
        """
        
        """


class Color:
    """
    Base class for colors.
    """
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def ToHex(self) -> str:
        """
        Converts this color 
        """
        def byte_to_hex(byte) -> str:
            """
            Converts from 0-255 to 00-FF
            """
            lookup = {
                0: "0",
                1: "1",
                2: "2",
                3: "3",
                4: "4",
                5: "5",
                6: "6",
                7: "7",
                8: "8",
                9: "9",
                10: "a",
                11: "b",
                12: "c",
                13: "d",
                14: "e",
                15: "f",
            }

            first_byte = byte // 16
            second_byte = byte % 16

            return f"{lookup[first_byte]}{lookup[second_byte]}"

        return f"#{byte_to_hex(self.r)}{byte_to_hex(self.g)}{byte_to_hex(self.b)}"


class FontStyles(IntFlag):
    Normal = 0
    Bold = 1
    Italic = 2
    Underline = 4
    Overstrike = 8

class Font:
    """
    Base class for fonts
    """
    def __init__(self, fontName: str, size: int, styles: FontStyles = FontStyles.Normal):
        self.fontName = fontName
        self.fontSize = size
        self.styles = styles

    def GetFont(self) -> CTkFont:
        isBold = FontStyles.Bold & self.styles
        isItalic = FontStyles.Italic & self.styles
        isUnderline = FontStyles.Underline & self.styles
        isOverstrike = FontStyles.Overstrike & self.styles

        return CTkFont(self.fontName,
            self.fontSize,
            weight="bold" if isBold else "normal",
            slant="italic" if isItalic else "roman",
            underline=True if isUnderline else False,
            overstrike=True if isOverstrike else False
        )

class Vector2:
    """
    Base class for coordinates
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Vector2Int:
    """
    Vector2 but is integer.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y