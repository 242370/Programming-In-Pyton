import math

from Sheep import Sheep
from Wolf import Wolf
import numpy as np


class Zad2:
    def __init__(self):
        # Simulation Constants
        self.absolute_value = 10.0
        self.number_of_rounds = 90
        self.number_of_sheep = 15
        self.sheep_movement_value = 0.5
        self.wolf_movement_value = 1.0
        # Actors
        self.wolf = Wolf()
        self.sheep = []
        for sheep in range(self.number_of_sheep):
            self.sheep.append(Sheep(self.absolute_value))

    def first_stage(self):
        for sheep in range(self.number_of_sheep):
            self.sheep[sheep].move(self.sheep_movement_value)

        shortest_distance = math.dist(self.wolf.position, self.sheep[0].position)
        closest_sheep_index = 0
        for sheep in range(1, self.number_of_sheep):
            current_distance = math.dist(self.wolf.position, self.sheep[sheep].position)
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                closest_sheep_index = sheep

        return shortest_distance, closest_sheep_index

    def second_stage(self, shortest_distance, closest_sheep_index):
        if shortest_distance <= self.wolf_movement_value:
            self.wolf.position = self.sheep[closest_sheep_index].position
            self.sheep.pop(closest_sheep_index)
            self.number_of_sheep -= 1

        else:
            direction_vector = ((self.sheep[closest_sheep_index].position[0] - self.wolf.position[0]) / shortest_distance,
                                (self.sheep[closest_sheep_index].position[1] - self.wolf.position[1]) / shortest_distance)

            self.wolf.move(self.wolf_movement_value, direction_vector)

    def start_simulation(self):
        for round in range(self.number_of_rounds):
            if self.number_of_sheep == 0:
                print('End')
                return

            shortest_distance, closest_sheep_index = self.first_stage()

            self.second_stage(shortest_distance, closest_sheep_index)
