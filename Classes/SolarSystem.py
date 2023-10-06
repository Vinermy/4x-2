from Classes.CelestialBody import CelestialBody, Star


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

