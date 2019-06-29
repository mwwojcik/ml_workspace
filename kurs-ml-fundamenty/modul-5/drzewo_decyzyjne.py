import sys
sys.path.insert(0, '../narzedzia/')
sys.path.insert(1, './wspolne/')

import pandas as pd
import sklearn.model_selection as ms
import sklearn.tree as tree
import sklearn.metrics as met
from raportowanie import raport
from wspolne.monitoring import  raportujParametryUczenia

def zamienDaneNieliczboweZeZmianaWymiarow(aDF):
    return pd.get_dummies(aDF)

#**** wczytanie danych
df=pd.read_csv('dane/breast-cancer.data',sep=',',header=None)


#**** przygotowanie danych
X_CANCER=df.iloc[:,1:10]
Y_CANCER=df.iloc[:,0]
X_CANCER_DUMM=zamienDaneNieliczboweZeZmianaWymiarow(X_CANCER)


#**** podzial na zbior treningowy i testowy
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_CANCER_DUMM,Y_CANCER,random_state=1,train_size=0.9, test_size=0.1)

#**** trening modelu
model=tree.DecisionTreeClassifier(max_depth=7)
model.fit(X_TRAIN,Y_TRAIN)

#walidacja
Y_PRED=model.predict(X_TEST)

#skutecznosc
skutecznosc=model.score(X_TEST,Y_TEST)
skutecznosc_na_zb_treningowym=model.score(X_TRAIN,Y_TRAIN)
#macierz pomylek
tn,fp,fn,tp=met.confusion_matrix(Y_TEST,Y_PRED).ravel()

raport('skutecznosc',skutecznosc)
raport('skutecznosc na zbiorze treningowym (roznica skutecznosci)',skutecznosc_na_zb_treningowym)
raport('roznica skutecznosci mowi o przeuczeniu','')
raport('TP(wynik-prawidlowy-pozytywnych)',tp)
raport('TP(wynik-prawidlowy-negatywnych)',tn)

raportujParametryUczenia(X_TRAIN,Y_TRAIN,X_TEST,Y_TEST,20)

