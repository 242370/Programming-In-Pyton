import pandas
import numpy as np


class Zad1:
    def __init__(self):
        self.data = pandas.read_csv("data.csv")
        self.qualitativeData = self.data[self.data.columns[0]]

    def genderof(self, index):
        return self.qualitativeData[index]

    def count_genders(self, gender):
        counter = 0
        for i in range(len(self.qualitativeData)):
            if self.genderof(i) == gender:
                counter += 1
        return counter

    def gender_percentage(self, gender):
        return round(self.count_genders(gender) / len(self.qualitativeData) * 100, 2)

    def generate_dataframe(self):
        final_data = [[self.count_genders('M'), self.gender_percentage('M')], [self.count_genders('I'), self.gender_percentage('I')],
                [self.count_genders('I'), self.gender_percentage('I')]]
        return pandas.DataFrame(final_data, index=['Male', 'Infant', 'Female'], columns=['count', '%'])
