import pandas
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sb

data = pandas.read_csv("data.csv", sep=',',
                       names=["Sex", "Length [mm]", "Diameter [mm]", "Height [mm]", "Whole weight [g]",
                              "Shucked weight [g]",
                              "Viscera weight [g]", "Shell weight [g]",
                              "Rings"])
qualitativeData = data[data.columns[0]]
quantitiveData = pandas.DataFrame(data[data.columns[1:]])


def sex_of(index):
    return qualitativeData[index]


def count_qualitative_occurrences(sex):
    counter = 0
    for i in range(len(qualitativeData)):
        if sex_of(i) == sex:
            counter += 1
    return counter


def qualitative_percentage(sex):
    return round(count_qualitative_occurrences(sex) / len(qualitativeData) * 100, 2)


def generate_qualitative_dataframe():
    final_data = [[count_qualitative_occurrences('M'), qualitative_percentage('M')],
                  [count_qualitative_occurrences('F'), qualitative_percentage('F')],
                  [count_qualitative_occurrences('I'), qualitative_percentage('I')]]
    return pandas.DataFrame(final_data, index=['Male', 'Infant', 'Female'], columns=['count', '%'])


def isolate_property(column):
    return quantitiveData[quantitiveData.columns[column]]


def generate_quantitive_dataframe():
    final_data = []
    for i in range(quantitiveData.shape[1]):
        property = isolate_property(i)
        final_data.append(
            [np.mean(property), np.std(property), np.min(property), np.quantile(property, [0.25]),
             np.median(property),
             np.quantile(property, [0.75]), np.max(property)])
    return pandas.DataFrame(final_data,
                            index=[quantitiveData.columns],
                            columns=['mean', 'std', 'min', '25%', '50%', '75%', 'max'])


def generate_qualitative_bar_chart(bar_width):
    x = ["Male", "Female", "Infant"]
    y = [count_qualitative_occurrences("M"), count_qualitative_occurrences('F'),
         count_qualitative_occurrences('I')]
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


def generate_quantitive_histogram(number_of_bins):
    figure, plot_number = plot.subplots(4, 2, layout='constrained')

    for row in range(0, 4):
        for col in range(0, 2):
            plot_number[row, col].hist(isolate_property(2 * row + col), bins=number_of_bins)
            title = quantitiveData.columns[2 * row + col]
            plot_number[row, col].set_title(title)

    for histogram in plot_number.flat:
        histogram.set(xlabel='Value', ylabel='Quantity')

    plot.show()


def generate_correlation_matrix():
    return quantitiveData.corr(method='pearson')


def generate_quantitive_scatter_plot():
    figure, plot_number = plot.subplots(14, 2, layout='constrained')

    row = 0
    col = 0
    for first_property in range(quantitiveData.shape[1]):
        for second_property in range(first_property + 1, quantitiveData.shape[1]):
            plot_number[row, col].scatter(isolate_property(first_property),
                                          isolate_property(second_property))
            title = quantitiveData.columns[first_property] + ' ' + quantitiveData.columns[second_property]
            plot_number[row, col].set_title(title)
            col = 1 - col
            if col == 0:
                row += 1

    plot.show()


def generate_heatmap():
    correlation_matrix = generate_correlation_matrix()
    sb.heatmap(correlation_matrix)
    plot.show()


def generate_linear_regression_plot():
    # TODO: not hardcoded values
    most_correlated_props = np.triu(generate_correlation_matrix(),
                                    1)  # triu - upper triangle, 1 - with diagonal
    most_correlated_props = most_correlated_props[np.triu_indices(quantitiveData.shape[1], -1)]

    sb.regplot(quantitiveData, x="Length [mm]", y="Diameter [mm]", line_kws={"color": "red"})
    plot.show()


# from ProgramInstance
# print(generate_qualitative_dataframe())
# print(generate_quantitive_dataframe())
# generate_qualitative_bar_chart(0.5)
# generate_quantitive_histogram(22)
# print(generate_correlation_matrix())
# generate_quantitive_scatter_plot()
# generate_heatmap()
generate_linear_regression_plot()
