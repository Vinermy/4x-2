class StarType:
    shortName: str
    minTemp: int
    maxTemp: int
    # MinMass and MaxMass are measured in solar masses
    minMass: float
    maxMass: float
    # MinRadius and MaxRadius are measured in solar radii
    minRadius: float
    maxRadius: float
    # MinLum and MaxLum are measures in solar luminosities
    minLum: float
    maxLum: float
    color: str
    verboseName: str

    def __init__(self,
                 shortName: str,
                 minTemp: int,
                 maxTemp: int,
                 minMass: float,
                 maxMass: float,
                 minRadius: float,
                 maxRadius: float,
                 minLum: float,
                 maxLum: float,
                 color: str,
                 verboseName: str):
        self.maxLum = maxLum
        self.minLum = minLum
        self.maxRadius = maxRadius
        self.minRadius = minRadius
        self.maxMass = maxMass
        self.minMass = minMass
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
