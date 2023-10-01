import time
from cmath import pi
from threading import Thread

from Classes.CelestialBody import Star, Planet
from graphics.FrameDrawer import Frame
from gui.MainWindow import MainWindow


class App:
    gui_thread: Thread
    frm = Frame()
    main_window: MainWindow

    def start(self):
        self.main_window = MainWindow("./gui/mainwindow.ui")
        self.gui_thread = Thread(target=self.main_window.display)
        self.gui_thread.start()
        while not self.main_window.is_loaded:
            pass
        obj = {
            "parameters": {
                "frame_xy": self.main_window.get_display_size(),
            },
            "objects": {
                "stars": [
                    Star(radius=0.7,
                         mass=1.9 * 10 ** 18,
                         luminosity=3.8 * 10 ** 14,
                         temperature=5772,
                         star_class="SG",
                         name="Sun")
                ],
                "planets": [
                    Planet(radius=0.006,
                           mass=6 * 10 ** 12,
                           temperature=273+15,
                           planet_type="EL",
                           name="Earth",
                           orbital_period=1,
                           orbital_radius=150000,
                           theta=.1,
                           host_body=Star(radius=0.7,
                                          mass=1.9 * 10 ** 18,
                                          luminosity=3.8 * 10 ** 14,
                                          temperature=5772,
                                          star_class="SG",
                                          name="Sun"))
                ]
            }
        }
        self.main_window.update_frame_image(self.frm.draw(objects=obj))


if __name__ == "__main__":
    app = App()
    app.start()
