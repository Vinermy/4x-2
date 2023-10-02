import json

from PIL import Image

from graphics.Drawers import StarDrawer, PlanetDrawer


class Frame:
    bg_color: tuple[int, int, int]

    def __init__(self):
        with open("./graphics/config.json") as con:
            c = json.load(con)
            self.bg_color = tuple(c["DRAWING-PARAMETERS"]["BACKGROUND-COLOR"])

    def draw(self, objects: dict) -> Image.Image:
        # Create image
        frame = Image.new("RGB", tuple(objects["parameters"]["frame_xy"]), self.bg_color)

        # Draw objects
        # Draw stars
        for star in objects["objects"]["stars"]:
            dr = StarDrawer(star, frame)
            dr.draw()

        for planet in objects["objects"]["planets"]:
            dr = PlanetDrawer(planet,  frame)
            dr.draw_orbit()
            dr.draw()

        return frame
