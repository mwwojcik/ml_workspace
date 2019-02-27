import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def drukujDaneDataSeta(dataset):
    # wymiary zestawu dancyh
    print(dataset.shape)

    # head - 20 pierwszych rekordow
    print(dataset.head(20))

    # descriptions dane statystyczne poszczegolnych atrybutow
    print(dataset.describe())

    # class distribution
    #print(dataset.groupby('class').size())


def pokazWykresyDataSeta(dataset):
    # box and whisker plots
    dataset.plot(kind='box', subplots=True,  sharex=False, sharey=False)
    plt.show()

    dataset.hist()
    plt.show()

    scatter_matrix(dataset)
    plt.show()