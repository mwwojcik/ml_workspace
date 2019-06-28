#*** ladowanie danych
import pandas as pd
import sklearn.model_selection as ms
from sklearn import tree
import  sklearn.metrics as met

# *** Wczytywanie danych

naglowki=pd.read_csv('dane/headers.csv',sep=',',header=None)
dane=pd.read_csv('dane/german.data',sep=' ',names=naglowki.iloc[0,:])
#dane=pd.read_csv('german.data',sep=',',header=None)
# *** Przygotowanie danych
# usuniecie pustych wierszy
dane=dane.dropna()

print(dane.shape)

# *** Podział danych na zbiory

#argumenty funkcji (cechy)
x_dane=dane.iloc[:,0:20]
x_dane_numeryczne=pd.get_dummies(x_dane)
#wartosci funkcji (wartosc ryzyka-ostatnia kolumna)
y_dane=dane.iloc[:,20]
#podział danych na czesc trenujaca i testowa
Xtrain,Xtest,Ytrain,Ytest=ms.train_test_split(x_dane_numeryczne,y_dane,random_state=1)


#*** Przygotowanie modelu
model=tree.DecisionTreeClassifier(max_depth=4,criterion='entropy',random_state=100)

#*** Trenowanie modelu
model.fit(Xtrain,Ytrain)

#predykcja danych testowych
wynik=model.score(Xtest,Ytest)
print('Poprawnosc modelu=>'+str(wynik))



# *** Optymalizacja
wyniki_dane_testowe=[]
wyniki_dane_treningowe=[]

for i in range(1,30):
    clf=tree.DecisionTreeClassifier(max_depth=i)
    clf.fit(Xtrain,Ytrain)
    wyniki_dane_testowe.append(clf.score(Xtest,Ytest))
    wyniki_dane_treningowe.append(clf.score(Xtrain,Ytrain))

import matplotlib.pyplot as plt
plt.plot(wyniki_dane_testowe,color='red')
plt.plot(wyniki_dane_treningowe)
plt.show()


