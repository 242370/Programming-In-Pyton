import json
import math

from Sheep import Sheep
from Wolf import Wolf
import numpy as np


class Zad2:
    def __init__(self):
        self.list_of_dicts = []
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
            self.sheep.append(Sheep(self.absolute_value, sheep + 1))

    def first_stage(self):
        for sheep in range(len(self.sheep)):
            self.sheep[sheep].move(self.sheep_movement_value)

        shortest_distance = math.dist(self.wolf.position, self.sheep[0].position)
        closest_sheep_index = 0
        for sheep in range(1, len(self.sheep)):
            current_distance = math.dist(self.wolf.position, self.sheep[sheep].position)
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                closest_sheep_index = sheep

        return shortest_distance, closest_sheep_index

    def second_stage(self, shortest_distance, closest_sheep_index):
        is_sheep_eaten = False
        if shortest_distance <= self.wolf_movement_value:
            self.wolf.position = self.sheep[closest_sheep_index].position
            self.sheep.pop(closest_sheep_index)
            self.number_of_sheep -= 1
            is_sheep_eaten = True

        else:
            direction_vector = ((self.sheep[closest_sheep_index].position[0] - self.wolf.position[0]) / shortest_distance,
                                (self.sheep[closest_sheep_index].position[1] - self.wolf.position[1]) / shortest_distance)

            self.wolf.move(self.wolf_movement_value, direction_vector)

        return is_sheep_eaten

    def print_data(self, round_number, focused_sheep, sheep_status):
        print('Current round: ' + str(round_number + 1))
        print('Wolf position: ' + str(round(self.wolf.position[0], 3)) + ';' + str(round(self.wolf.position[1], 3)))
        print('Number of Sheep alive: ' + str(len(self.sheep)))
        if sheep_status:
            print('Sheep number ' + str(focused_sheep) + ' was eaten')
        else:
            print('Sheep number ' + str(focused_sheep) + ' is being chased')
        print('')

    def save_to_json(self, round_number):
        sheep_pos = []
        for sheep_sequence_number in range(self.number_of_sheep):
            is_sheep_eaten = True
            for sheep in range(len(self.sheep)):
                if sheep_sequence_number + 1 == self.sheep[sheep].sequence_number:
                    sheep_pos.append(self.sheep[sheep].position)
                    is_sheep_eaten = False
                    break

            if is_sheep_eaten:
                sheep_pos.append(None)

        current_round_data = {"round_no": round_number,
                              "wolf_pos": self.wolf.position,
                              "sheep_pos": sheep_pos}

        self.list_of_dicts.append(current_round_data)

    def start_simulation(self):
        open("pos.json", "w").close()

        for round_number in range(self.number_of_rounds):
            if len(self.sheep) == 0:
                print('All sheep are eaten')
                with open("pos.json", "w") as outfile:
                    outfile.write(json.dumps(self.list_of_dicts, indent=4))
                return

            shortest_distance, closest_sheep_index = self.first_stage()
            focused_sheep = self.sheep[closest_sheep_index].sequence_number

            is_sheep_eaten = self.second_stage(shortest_distance, closest_sheep_index)

            self.print_data(round_number, focused_sheep, is_sheep_eaten)

            self.save_to_json(round_number)

        print('Some sheep managed to escape')
        with open("pos.json", "w") as outfile:
            outfile.write(json.dumps(self.list_of_dicts, indent=4))
