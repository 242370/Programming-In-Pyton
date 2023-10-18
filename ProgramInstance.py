from Zad1 import Zad1

if __name__ == '__main__':
    snails = Zad1()
    qualitive_dataframe = snails.generate_qualitive_dataframe()
    print(qualitive_dataframe)
    quantitive_dataframe = snails.generate_quantitive_dataframe()
    print(quantitive_dataframe)
