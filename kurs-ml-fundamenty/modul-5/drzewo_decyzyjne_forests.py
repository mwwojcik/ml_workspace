import sys
sys.path.insert(0, '../narzedzia/')
sys.path.insert(1, './wspolne/')

import pandas as pd
import sklearn.model_selection as ms
import sklearn.ensemble as ensemble
import matplotlib.pyplot as plt
from raportowanie import raport,printdf,headdf

#**** wczytanie danych
df=pd.read_csv('dane/Social_Network_Ads.csv',sep=',',header=0)


#**** przygotowanie danych
X_SOCIAL=df[['Age','EstimatedSalary']]
Y_SOCIAL=df[['Purchased']]

printdf(X_SOCIAL)

#**** podzial na zbior treningowy i testowy
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_SOCIAL,Y_SOCIAL,test_size=0.2,random_state=10)


#**** trening modelu
model=ensemble.RandomForestClassifier(n_estimators=300,criterion='gini',random_state=0)
model.fit(X_TRAIN,Y_TRAIN)

#walidacja
Y_PRED=model.predict(X_TEST)

#skutecznosc
skutecznosc=model.score(X_TEST,Y_TEST)
raport('skutecznosc',skutecznosc)

plt.plot(Y_TEST)
plt.plot(Y_PRED,color='red')
plt.show()

