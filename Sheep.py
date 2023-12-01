import random


class Sheep:
    def __init__(self, absolute_value: float):
        self.initial_position = (round(random.uniform(-absolute_value, absolute_value), 1),
                                 round(random.uniform(-absolute_value, absolute_value), 1))
        self.directions = {1: 'Up', 2: 'Right', 3: 'Down', 4: 'Left'}

    def move(self, movement_value):

