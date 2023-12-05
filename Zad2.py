import csv
import json
import math
import os.path

from Sheep import Sheep
from Wolf import Wolf


class Zad2:
    def __init__(self):
        # Results
        self.list_of_dicts = []
        self.json_file = 'pos.json'
        self.csv_file = 'alive.csv'
        # Simulation Constants
        self.absolute_value = 10.0
        self.number_of_rounds = 50
        self.number_of_sheep = 15
        self.sheep_movement_value = 0.5
        self.wolf_movement_value = 1.0
        # Actors
        self.wolf = Wolf()
        self.sheep = {}
        for sheep in range(self.number_of_sheep):
            self.sheep[sheep] = Sheep(self.absolute_value, sheep)

    def first_stage(self):
        for sheep in self.sheep.values():
            sheep.move(self.sheep_movement_value)

        shortest_distance = float('inf')
        closest_sheep_key = -1

        for sheep in self.sheep.items():
            # sheep: Tuple(int, Sheep)
            current_distance = math.dist(self.wolf.position, sheep[1].position)
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                closest_sheep_key = sheep[0]

        return shortest_distance, closest_sheep_key

    def second_stage(self, shortest_distance, closest_sheep_key):
        is_sheep_eaten = False
        if shortest_distance <= self.wolf_movement_value:
            self.wolf.position = self.sheep[closest_sheep_key].position
            self.sheep.pop(closest_sheep_key)
            is_sheep_eaten = True

        else:
            direction_vector = ((self.sheep[closest_sheep_key].position[0] - self.wolf.position[0]) / shortest_distance,
                                (self.sheep[closest_sheep_key].position[1] - self.wolf.position[1]) / shortest_distance)

            self.wolf.move(self.wolf_movement_value, direction_vector)

        return is_sheep_eaten

    def print_data(self, round_number, closest_sheep_key, is_sheep_eaten):
        print('Current round: ' + str(round_number + 1))
        print('Wolf position: ' + str(round(self.wolf.position[0], 3)) + ';' + str(round(self.wolf.position[1], 3)))
        print('Number of Sheep alive: ' + str(len(self.sheep)))

        if is_sheep_eaten:
            print('Sheep number ' + str(closest_sheep_key) + ' was eaten')
        else:
            print('Sheep number ' + str(closest_sheep_key) + ' is being chased')
        print('')

    def save_to_json(self, round_number):
        sheep_pos = []
        for sheep_sequence_number in range(self.number_of_sheep):
            if self.sheep.get(sheep_sequence_number) is None:
                sheep_pos.append(None)
            else:
                sheep_pos.append(self.sheep[sheep_sequence_number].position)

        current_round_data = {"round_no": round_number + 1,
                              "wolf_pos": self.wolf.position,
                              "sheep_pos": sheep_pos}

        self.list_of_dicts.append(current_round_data)

    def save_to_csv(self, round_number):
        with open(self.csv_file, "a", newline='') as outfile:
            file_writer = csv.writer(outfile)
            if round_number == 0:
                file_writer.writerow(["round_no", "alive_sheep"])
            file_writer.writerow([round_number + 1, len(self.sheep)])

    def start_simulation(self):
        if os.path.isfile(self.json_file):
            os.remove(self.json_file)
        if os.path.isfile(self.csv_file):
            os.remove(self.csv_file)

        for round_number in range(self.number_of_rounds):
            if len(self.sheep) == 0:
                print('All sheep are eaten')
                with open(self.json_file, "w") as outfile:
                    outfile.write(json.dumps(self.list_of_dicts, indent=4))
                return

            shortest_distance, closest_sheep_key = self.first_stage()
            is_sheep_eaten = self.second_stage(shortest_distance, closest_sheep_key)

            self.print_data(round_number, closest_sheep_key, is_sheep_eaten)

            self.save_to_json(round_number)

            self.save_to_csv(round_number)

        print('Some sheep managed to escape')
        with open(self.json_file, "w") as outfile:
            outfile.write(json.dumps(self.list_of_dicts, indent=4))
