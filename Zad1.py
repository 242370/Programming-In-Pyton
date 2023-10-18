import pandas
import numpy as np
import Arrays


class Zad1:
    def __init__(self):
        self.data = pandas.read_csv("data.csv", header=None)
        self.qualitativeData = self.data[self.data.columns[0]]
        self.quantitiveData = self.data[self.data.columns[1:]]

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

    def generate_qualitive_dataframe(self):
        final_data = [[self.count_genders('M'), self.gender_percentage('M')], [self.count_genders('I'), self.gender_percentage('I')],
                      [self.count_genders('I'), self.gender_percentage('I')]]
        return pandas.DataFrame(final_data, index=['Male', 'Infant', 'Female'], columns=['count', '%'])

    def isolate_property(self, column):
        self.quantitiveData = pandas.DataFrame(self.quantitiveData)
        return self.quantitiveData[self.quantitiveData.columns[column]]

    #TODO: needs quartiles
    def generate_quantitive_dataframe(self):
        final_data = []
        for i in range(self.quantitiveData.shape[1]):
            property = self.isolate_property(i)
            final_data.append([np.mean(property), np.std(property), np.min(property), np.median(property), np.max(property)])
        return pandas.DataFrame(final_data,
                                index=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'],
                                columns=['mean', 'std', 'min', '50%', 'max'])



