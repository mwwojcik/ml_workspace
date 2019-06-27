#*** ladowanie danych
import pandas as pd
import sklearn.model_selection as ms
from sklearn import tree
import  sklearn.metrics as met

# *** Wczytywanie danych

naglowki=pd.read_csv('headers.csv',sep=',',header=None)
#dane=pd.read_csv('german.data',sep=' ',names=naglowki.iloc[0,:])
dane=pd.read_csv('german-numeric.data',sep=',',header=None)
# *** Przygotowanie danych
# usuniecie pustych wierszy
dane=dane.dropna()

print(dane.shape)

# *** Podział danych na zbiory

#argumenty funkcji (cechy)
x_dane=dane.iloc[:,0:23]
#wartosci funkcji (wartosc ryzyka-ostatnia kolumna)
y_dane=dane.iloc[:,23:24]
#podział danych na czesc trenujaca i testowa
Xtrain,Xtest,Ytrain,Ytest=ms.train_test_split(x_dane,y_dane,random_state=1)


#*** Przygotowanie modelu
model=tree.DecisionTreeClassifier()

#*** Trenowanie modelu
model.fit(Xtrain,Ytrain)

#predykcja danych testowych
result=model.predict(Xtest)
wynik=met.accuracy_score(Ytest,result)

print(wynik)


