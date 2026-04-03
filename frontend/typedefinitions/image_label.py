from PIL import Image, ImageTk
import customtkinter as ctk
from .base import *

class ImageLabel(UIElement):
    def __init__(
            self,
            position: Vector2,
            imageSize: Vector2Int,
            imagePath: str,
            anchor: ElementAlign = ElementAlign.NoAlign,
            useRelativePos: bool = True,
        ):
        
        super().__init__(position, anchor, useRelativePos)
        self.imageSize = imageSize
        self.imagePath = imagePath
        self.useRelativePos = useRelativePos
    
    def Draw(self, wd: Window):
        image = Image.open(self.imagePath).resize((self.imageSize.x, self.imageSize.y))
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(self.imageSize.x, self.imageSize.y))

        label = ctk.CTkLabel(wd.wd, image=ctk_image, text="", fg_color="transparent")

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