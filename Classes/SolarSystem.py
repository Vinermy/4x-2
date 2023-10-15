import numpy.random as rng
from scipy.stats import truncnorm

from Classes.CelestialBody import CelestialBody, Star, STAR_TYPES, Planet
from Classes.HelpClasses import StarType


def get_truncated_normal(mean: float, low: float, upp: float):
    return truncnorm(
        (low - mean) / 1,
        (upp - mean) / 1,
        loc=mean, scale=1
    ).rvs()


class CelestialBSystem:
    name: str
    host_body: CelestialBody
    orbiting_bodies = list

    def __init__(self, name: str, host_body: CelestialBody, orbiting_bodies: list):
        self.name = name
        self.host_body = host_body
        self.orbiting_bodies = orbiting_bodies


class StarSystem(CelestialBSystem):
    host_body: Star


def generate_system(name: str) -> StarSystem:
    # SYSTEM LEVEL
    # PHASE 1 - STAR GENERATION
    classes_domain = list(STAR_TYPES.keys())
    classes_probs = [
        .0001,  # Class O stars
        .0100,  # Class B stars
        .0060,  # Class A stars
        .0239,  # Class F stars
        .0800,  # Class G stars
        .1200,  # Class K stars
        .7600,  # Class M stars
    ]
    s_class: str = rng.choice(classes_domain,
                              size=1,
                              replace=False,
                              p=classes_probs).item(0)
    s_class: StarType = STAR_TYPES[s_class]

    temperature = get_truncated_normal(
        mean=(s_class.minTemp + s_class.maxTemp) / 2,
        low=s_class.minTemp,
        upp=s_class.maxTemp
    )

    mass = get_truncated_normal(
        mean=(s_class.minMass + s_class.maxMass) / 2,
        low=s_class.minMass,
        upp=s_class.maxMass
    ) * 1.99 * 10 ** 18  # Convert from solar masses

    radius = get_truncated_normal(
        mean=(s_class.minRadius + s_class.maxRadius) / 2,
        low=s_class.minRadius,
        upp=s_class.maxRadius
    ) * 6.96 * 10 ** 2  # Convert from solar radii to 10^6 meters

    luminosity = get_truncated_normal(
        mean=(s_class.minLum + s_class.maxLum) / 2,
        low=s_class.minLum,
        upp=s_class.maxLum
    ) * 3.83 * 10 ** 14  # Convert from solar luminosities

    star = Star(
        name=f"{s_class.shortName[1]}-{rng.randint(low=1000, high=10000)}",
        star_class=s_class.shortName,
        mass=mass,
        radius=radius,
        temperature=temperature,
        luminosity=luminosity
    )

    # PHASE 2 - SYSTEM GENERATION
    planet_number = int(get_truncated_normal(3, 1, 6))
    planets: list[Planet] = []
    planet_mass_max = 9.5 * 10 ** -4 * star.mass
    planet_mass_mean = 3 * 10 ** -6 * star.mass
    planet_mass_min = .5 * 10 ** -9 * star.mass
    belt_threshold = 1.2 * 10 ** -9 * star.mass

    for i in range(planet_number):
        mass = get_truncated_normal(
            mean=planet_mass_mean,
            low=planet_mass_min,
            upp=planet_mass_max
        )

        if mass > belt_threshold:
            # GENERATE A PLANET
            pass
        else:
            # GENERATE AN ASTEROID BELT
            pass

    system = StarSystem(
        name=name,
        host_body=star,
        orbiting_bodies=[]
    )
    return system
