import random


class Sheep:
    def __init__(self, absolute_value: float, sequence_number):
        self.position = (round(random.uniform(-absolute_value, absolute_value), 1),
                         round(random.uniform(-absolute_value, absolute_value), 1))
        self.directions = ('Up', 'Right', 'Down', 'Left')
        self.sequence_number = sequence_number

    def move(self, movement_value):
        current_direction = random.choice(self.directions)
        if current_direction == 'Up':
            self.position = (self.position[0], self.position[1] + movement_value)
        elif current_direction == 'Right':
            self.position = (self.position[0] + movement_value, self.position[1])
        elif current_direction == 'Down':
            self.position = (self.position[0], self.position[1] - movement_value)
        else:
            self.position = (self.position[0] - movement_value, self.position[1])
