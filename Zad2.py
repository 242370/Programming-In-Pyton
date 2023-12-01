from Sheep import Sheep
from Wolf import Wolf


class Zad2:
    def __init__(self):
        # Simulation Constants
        self.absolute_value = 10.0
        self.number_of_rounds = 50
        self.number_of_sheep = 15
        self.sheep_movement_distance = 0.5
        self.wolf_movement_distance = 1.0
        # Actors
        self.wolf = Wolf()
        self.sheep = []
        for sheep in range(self.number_of_sheep):
            self.sheep.append(Sheep(self.absolute_value))
