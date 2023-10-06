import json

from PIL import Image
from PIL.ImageDraw import ImageDraw

from Classes.SolarSystem import StarSystem
from graphics.Drawers import StarSystemDrawer


class Frame:
    bg_color: tuple[int, int, int]

    def __init__(self):
        with open("./graphics/config.json") as con:
            c = json.load(con)
            self.bg_color = tuple(c["DRAWING-PARAMETERS"]["BACKGROUND-COLOR"])

    def draw(self, system: StarSystem, xy: tuple[int, int]) -> Image.Image:
        # Create image
        frame = Image.new("RGB", xy, self.bg_color)
        draw = ImageDraw(frame, "RGB")

        drawer = StarSystemDrawer(system, frame)
        drawer.draw()

        draw.text((10, 10), system.name, fill=(255, 255, 255))

        return frame
