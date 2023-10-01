from math import inf


class StarType:
    shortName: str
    minTemp: int
    maxTemp: int | type(inf)
    color: str
    verboseName: str

    def __init__(self, shortName: str, minTemp: int, maxTemp: int | type(inf), color: str, verboseName: str) -> None:
        self.shortName = shortName
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.color = color
        self.verboseName = verboseName


class PlanetType:
    shortName: str
    verboseName: str
    buildable_surface: float
    resource_generation_chance: float
    max_resource_deposits: int  # This parameter represents only the relative resource density on the planet,
    # the absolute value is generated with respect to planet size

    def __init__(self, verboseName: str, buildable_surface: float, resource_generation_chance: float,
                 max_resource_deposits: int):
        self.verboseName = verboseName
        self.buildable_surface = buildable_surface
        self.resource_generation_chance = resource_generation_chance
        self.max_resource_deposits = max_resource_deposits
