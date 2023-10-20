import pandas
import numpy as np
import matplotlib.pyplot as plot


class Zad1:
    def __init__(self):
        self.data = pandas.read_csv("data.csv", sep=',',
                                    names=["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight",
                                           "Rings"])
        self.qualitativeData = self.data[self.data.columns[0]]
        self.quantitiveData = pandas.DataFrame(self.data[self.data.columns[1:]])

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
        return self.quantitiveData[self.quantitiveData.columns[column]]

    def generate_quantitive_dataframe(self):
        final_data = []
        for i in range(self.quantitiveData.shape[1]):
            property = self.isolate_property(i)
            final_data.append(
                [np.mean(property), np.std(property), np.min(property), np.quantile(property, [0.25]), np.median(property),
                 np.quantile(property, [0.75]), np.max(property)])
        return pandas.DataFrame(final_data,
                                index=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight',
                                       'Rings'],
                                columns=['mean', 'std', 'min', '25%', '50%', '75%', 'max'])

    def generate_qualitative_bar_chart(self):
        x = ["Male", "Female", "Infant"]
        y = [self.count_genders("M"), self.count_genders('F'), self.count_genders('I')]
        plot.bar(x[0], y[0], color="blue", width=0.5)
        plot.bar(x[1], y[1], color="red", width=0.5)
        plot.bar(x[2], y[2], color="green", width=0.5)
        plot.xlabel("Sex")
        plot.ylabel("Quantity")
        plot.title("Qualitative variable occurrences")
        plot.text(x[0], y[0], str(y[0]), ha='center')  # ha - horizontal alignment
        plot.text(x[1], y[1], str(y[1]), ha='center')
        plot.text(x[2], y[2], str(y[2]), ha='center')
        plot.show()

    def generate_quantitive_histogram(self, number_of_bins):
        figure, plot_number = plot.subplots(4, 2, layout='constrained')

        for i in range(0, 4):
            for j in range(0, 2):
                plot_number[i, j].hist(self.isolate_property(2 * i + j), bins=number_of_bins)
                title = self.quantitiveData.columns[2 * i + j]
                plot_number[i, j].set_title(title)

        for histogram in plot_number.flat:
            histogram.set(xlabel='Value', ylabel='Quantity')

        plot.show()

    def generate_correlation_matrix(self):
        matrix = self.quantitiveData.corr(method='pearson')
        return matrix
