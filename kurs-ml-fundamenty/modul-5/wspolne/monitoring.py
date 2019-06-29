import sklearn.tree as tree
import matplotlib.pyplot as plt

def raportujParametryUczenia(aXtrain,aYtrain,aXtest,aYtest,liczba_iteracji):
    # *** Optymalizacja
    wyniki_dane_testowe = []
    wyniki_dane_treningowe = []

    for i in range(1, liczba_iteracji):
        clf = tree.DecisionTreeClassifier(max_depth=i)
        clf.fit(aXtrain, aYtrain)
        wyniki_dane_testowe.append(clf.score(aXtest, aYtest))
        wyniki_dane_treningowe.append(clf.score(aXtrain, aYtrain))

    plt.plot(wyniki_dane_testowe, color='red')
    plt.plot(wyniki_dane_treningowe)
    plt.show()