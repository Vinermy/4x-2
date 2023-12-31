import json

from PIL import ImageDraw
from PIL.Image import Image

from Classes.CelestialBody import Star, Planet
from Classes.SolarSystem import StarSystem


def draw_circle_by_center_and_radius(d: ImageDraw.ImageDraw, center_x: int, center_y: int, radius: int,
                                     color: tuple[int, int, int] = (0, 0, 0), border: tuple[int, int, int] = (0, 0, 0)):
    x0 = center_x - radius
    x1 = center_x + radius
    y0 = center_y - radius
    y1 = center_y + radius
    d.ellipse([x0, y0, x1, y1], fill=color if color != (0, 0, 0) else None,
              outline=border if border != (0, 0, 0) else None, width=1)


def display_name(d: ImageDraw.ImageDraw, xy: tuple[int, int], name: str):
    d.text(
        xy, name
    )


class StarDrawer:
    star: Star
    draw_object: ImageDraw.ImageDraw
    color: tuple[int, int, int]
    scale_factor: float
    translate: list[int, int]

    def __init__(self, star: Star, image: Image):
        self.star = star
        self.draw_object = ImageDraw.Draw(image)
        self.translate = [image.width // 2, image.height // 2]

        with open("./graphics/config.json") as config:
            c = json.load(config)
            self.color = tuple(c["STAR-COLORS"][self.star.star_class.shortName])
            self.body_scale_factor = float(c["DRAWING-PARAMETERS"]["BODY-SCALE-FACTOR"])
            self.scale_factor = float(c["DRAWING-PARAMETERS"]["SCALE-FACTOR"])

    def draw(self):
        x = self.star.x * self.scale_factor + self.translate[0]
        y = self.star.y * self.scale_factor + self.translate[1]
        radius = int(self.star.radius * self.body_scale_factor)
        draw_circle_by_center_and_radius(self.draw_object, x, y, radius,
                                         self.color)
        display_name(self.draw_object, (x + radius, y + radius), self.star.name)


class PlanetDrawer:
    planet: Planet
    draw_object: ImageDraw.ImageDraw
    color: tuple[int, int, int]
    scale_factor: float
    translate: list[int, int]

    def __init__(self, planet: Planet, image: Image):
        self.planet = planet
        self.draw_object = ImageDraw.Draw(image)
        self.translate = [image.width // 2, image.height // 2]

        with open("./graphics/config.json") as config:
            c = json.load(config)
            self.color = tuple(c["PLANET-COLORS"][self.planet.planet_type])
            self.orbit_color = tuple(c["DRAWING-PARAMETERS"]["ORBIT-COLOR"])
            self.body_scale_factor = float(c["DRAWING-PARAMETERS"]["BODY-SCALE-FACTOR"])
            self.scale_factor = float(c["DRAWING-PARAMETERS"]["SCALE-FACTOR"])

    def draw(self):
        xy = self.planet.calculate_xy()
        x = int(xy[0] * self.scale_factor) + self.translate[0]
        y = int(xy[1] * self.scale_factor) + self.translate[1]
        radius = max(int(self.planet.radius * self.body_scale_factor), 5)
        draw_circle_by_center_and_radius(self.draw_object, x, y, radius,
                                         self.color)
        display_name(self.draw_object, (x + radius, y + radius), self.planet.name)

    def draw_orbit(self):
        x = int(self.planet.host_body.x * self.scale_factor) + self.translate[0]
        y = int(self.planet.host_body.y * self.scale_factor) + self.translate[1]
        draw_circle_by_center_and_radius(self.draw_object, x, y, int(self.planet.orbital_radius * self.scale_factor),
                                         border=self.orbit_color)


class StarSystemDrawer:
    def __init__(self, system: StarSystem, image: Image):
        self.system = system
        self.image = image

    def draw(self):
        sd = StarDrawer(self.system.host_body, self.image)
        sd.draw()

        for body in self.system.orbiting_bodies:
            match type(body):
                case Planet:
                    d = PlanetDrawer(body, self.image)
                    d.draw_orbit()
                    d.draw()
