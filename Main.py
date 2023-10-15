import sys

from PySide6.QtWidgets import QApplication

from Classes.CelestialBody import Star, Planet
from Classes.SolarSystem import StarSystem
from graphics.FrameDrawer import Frame
from gui.MainWindow import MainWindow


class App:
    frm = Frame()
    main_window: MainWindow

    def start(self):
        sun = Star(radius=700,
                   mass=1.9 * 10 ** 18,
                   luminosity=3.8 * 10 ** 14,
                   temperature=5772,
                   star_class="SG",
                   name="Sun",
                   )

        planet = Planet(radius=.006,
                        mass=6 * 10 ** 12,
                        temperature=288,
                        planet_type="EL",
                        name="Earth",
                        orbital_period=1,
                        orbital_radius=150000,
                        theta=0,
                        host_body=sun)

        system = StarSystem("Solar system", sun, [planet])

        self.display_window(system)

    def display_window(self, system):
        app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.current_system = system
        self.main_window.display(app)


if __name__ == "__main__":
    app = App()
    app.start()
