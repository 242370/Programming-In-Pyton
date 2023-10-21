import pandas
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sb


class Zad1:
    def __init__(self):
        self.data = pandas.read_csv("data.csv", sep=',',
                                    names=["Sex", "Length [mm]", "Diameter [mm]", "Height [mm]", "Whole weight [g]", "Shucked weight [g]",
                                           "Viscera weight [g]", "Shell weight [g]",
                                           "Rings"])
        self.qualitativeData = self.data[self.data.columns[0]]
        self.quantitiveData = pandas.DataFrame(self.data[self.data.columns[1:]])

    def sex_of(self, index):
        return self.qualitativeData[index]

    def count_qualitative_occurrences(self, sex):
        counter = 0
        for i in range(len(self.qualitativeData)):
            if self.sex_of(i) == sex:
                counter += 1
        return counter

    def qualitative_percentage(self, sex):
        return round(self.count_qualitative_occurrences(sex) / len(self.qualitativeData) * 100, 2)

    def generate_qualitative_dataframe(self):
        final_data = [[self.count_qualitative_occurrences('M'), self.qualitative_percentage('M')],
                      [self.count_qualitative_occurrences('F'), self.qualitative_percentage('F')],
                      [self.count_qualitative_occurrences('I'), self.qualitative_percentage('I')]]
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
                                index=[self.quantitiveData.columns],
                                columns=['mean', 'std', 'min', '25%', '50%', '75%', 'max'])

    def generate_qualitative_bar_chart(self, bar_width):
        x = ["Male", "Female", "Infant"]
        y = [self.count_qualitative_occurrences("M"), self.count_qualitative_occurrences('F'), self.count_qualitative_occurrences('I')]
        plot.bar(x[0], y[0], color="blue", width=bar_width)
        plot.bar(x[1], y[1], color="red", width=bar_width)
        plot.bar(x[2], y[2], color="green", width=bar_width)
        plot.xlabel("Sex")
        plot.ylabel("Quantity")
        plot.title("Qualitative variable occurrences")
        plot.text(x[0], y[0], str(y[0]), ha='center')  # ha - horizontal alignment
        plot.text(x[1], y[1], str(y[1]), ha='center')
        plot.text(x[2], y[2], str(y[2]), ha='center')
        plot.show()

    def generate_quantitive_histogram(self, number_of_bins):
        figure, plot_number = plot.subplots(4, 2, layout='constrained')

        for row in range(0, 4):
            for col in range(0, 2):
                plot_number[row, col].hist(self.isolate_property(2 * row + col), bins=number_of_bins)
                title = self.quantitiveData.columns[2 * row + col]
                plot_number[row, col].set_title(title)

        for histogram in plot_number.flat:
            histogram.set(xlabel='Value', ylabel='Quantity')

        plot.show()

    def generate_correlation_matrix(self):
        return self.quantitiveData.corr(method='pearson')

    # TODO: Should work but doesn't xD
    def generate_quantitive_scatter_plot(self):
        figure, plot_number = plot.subplots(14, 2, layout='constrained')
        plots = []

        for first_property in range(self.quantitiveData.shape[1]):
            for second_property in range(first_property + 1, self.quantitiveData.shape[1]):
                plots.append(plot.scatter(self.isolate_property(first_property), self.isolate_property(second_property)))

        for row in range(0, 14):
            for col in range(0, 2):
                plot_number[row, col] = plots.pop(0)

        plot.show()

    def generate_heatmap(self):
        correlation_matrix = self.generate_correlation_matrix()
        sb.heatmap(correlation_matrix)
        plot.show()

    def generate_linear_regression_plot(self):
        # TODO: not hardcoded values
        most_correlated_props = np.triu(self.generate_correlation_matrix(), 1)  # triu - upper triangle, 1 - with diagonal
        most_correlated_props = most_correlated_props[np.triu_indices(self.quantitiveData.shape[1], -1)]

        sb.regplot(self.quantitiveData, x="Length [mm]", y="Diameter [mm]", line_kws={"color": "red"})
        plot.show()
