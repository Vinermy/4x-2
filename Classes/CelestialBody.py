from math import inf, pi, cos, sin
from .HelpClasses import StarType, PlanetType

# CONSTANTS
BUILDABLE_SURFACE_MULTIPLIER: float = .001

STAR_TYPES: dict[str:StarType] = {
    "SO": StarType(shortName="SO",
                   minTemp=30001,
                   maxTemp=inf,
                   color="Blue",
                   verboseName="O class star"),
    "SB": StarType(shortName="SB",
                   minTemp=10001,
                   maxTemp=30000,
                   color="White-blue",
                   verboseName="B class star"),
    "SA": StarType(shortName="SA",
                   minTemp=7401,
                   maxTemp=10000,
                   color="White",
                   verboseName="A class star"),
    "SF": StarType(shortName="SF",
                   minTemp=6001,
                   maxTemp=7400,
                   color="Yellow-white",
                   verboseName="F class star"),
    "SG": StarType(shortName="SG",
                   minTemp=5001,
                   maxTemp=6000,
                   color="Yellow",
                   verboseName="G class star"),
    "SK": StarType(shortName="SK",
                   minTemp=3801,
                   maxTemp=5000,
                   color="Orange",
                   verboseName="K class star"),
    "SM": StarType(shortName="SM",
                   minTemp=2501,
                   maxTemp=3800,
                   color="Red",
                   verboseName="M class star"),
    "SL": StarType(shortName="SL",
                   minTemp=1301,
                   maxTemp=2500,
                   color="Dark red",
                   verboseName="L class star"),
    "ST": StarType(shortName="ST",
                   minTemp=601,
                   maxTemp=1300,
                   color="Dark red",
                   verboseName="T class star"),
    "SY": StarType(shortName="SY",
                   minTemp=0,
                   maxTemp=600,
                   color="Dark red",
                   verboseName="Y class star"),
}

PLANET_TYPES: [dict[str:PlanetType]] = {
    "EL": PlanetType(verboseName="Earth-like",
                     buildable_surface=.05,
                     resource_generation_chance=.85,
                     max_resource_deposits=3),

    "DS": PlanetType(verboseName="Deserted",
                     buildable_surface=.12,
                     resource_generation_chance=.69,
                     max_resource_deposits=5),

    "IC": PlanetType(verboseName="Ice-covered",
                     buildable_surface=.02,
                     resource_generation_chance=.56,
                     max_resource_deposits=2),

    "GG": PlanetType(verboseName="Gas giant",
                     buildable_surface=0,
                     resource_generation_chance=1,
                     max_resource_deposits=2)
}


# --------------------

class CelestialBody(object):
    name: str
    mass: float  # is measured in 10^12 kg
    radius: float  # is measured in 10^6 m
    temperature: float  # is measured in Kelvins (praise the Lord Kelvin!)
    x: float  # Coordinates inside a solar system. Stars sit at (0,0), unless they are double
    y: float  # Measured in 10^6 m


class Star(CelestialBody):
    luminosity: float  # is measured in 10^12 Wt
    star_class: StarType

    x = 0
    y = 0

    def set_class(self, star_class: str):
        try:
            self.star_class = STAR_TYPES[star_class]
        except KeyError:
            raise KeyError(f"Incorrect star class - {star_class}")

    def __init__(self, luminosity, temperature, star_class, radius, mass, name):
        self.luminosity = luminosity
        self.temperature = temperature
        self.set_class(star_class)
        self.radius = radius
        self.mass = mass
        self.name = name


class OrbitingBody(CelestialBody):
    host_body: CelestialBody
    orbital_radius: float
    orbital_period: float  # is measured in years
    theta: float = 0

    def calculate_movement(self, time) -> float:
        velocity = 2 * pi / self.orbital_period  # radians per year
        moved = velocity * time  # radians
        self.theta += moved
        return self.theta

    def calculate_xy(self) -> list[float, float]:
        th: float = self.theta % (2 * pi)
        return [float(self.orbital_radius * cos(th)) + self.host_body.x,
                float(self.orbital_radius * sin(th)) + self.host_body.y]


class Planet(OrbitingBody):
    planet_type: str
    type: PlanetType

    def __init__(self, temperature, planet_type, radius, mass, name, orbital_radius: float, orbital_period: float,
                 theta: float, host_body: CelestialBody):
        self.temperature = temperature
        self.planet_type = planet_type
        self.set_planet_type(planet_type)
        self.radius = radius
        self.mass = mass
        self.name = name
        self.host_body = host_body
        self.orbital_radius = orbital_radius
        self.orbital_period = orbital_period
        self.theta = theta
        self.x, self.y = self.calculate_xy()

    def get_max_buildings(self):
        return self.radius ** 2 * pi * 4 * PLANET_TYPES[self.planet_type][
            "buildable_surface"] * BUILDABLE_SURFACE_MULTIPLIER

    def set_planet_type(self, planet_type: str):
        try:
            self.type = PLANET_TYPES[planet_type]
        except KeyError:
            raise KeyError(f"Incorrect planet type - {planet_type}")
