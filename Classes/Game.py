from Classes.SolarSystem import StarSystem, generate_system
from datetime import datetime


class Game:
    systems: list[StarSystem]
    current_date: datetime
    current_system: StarSystem
    capital: StarSystem
    empire_name: str
    capital_name: str

    def new(self, current_date, empire_name, capital_name):
        self.capital_name = capital_name
        self.empire_name = empire_name
        self.current_date = current_date
        self.capital = generate_system(self.capital_name)
        self.current_system = self.capital

