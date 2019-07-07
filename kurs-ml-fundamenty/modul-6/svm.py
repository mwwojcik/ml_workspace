import sys
sys.path.insert(0, '../narzedzia/')
from raportowanie import raport,printdf,headdf
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
import sklearn.model_selection as ms
from  sklearn import svm
from sklearn import metrics as met

df=pd.read_csv('dane/caesarian.csv',sep=',',header=0)

X_CES=df.iloc[:,0:5]
Y_CES=df.iloc[:,5]

deliveryTimeMap={
    0:'timely',
    1:'premature',
    2:'latecomer'
}

X_CES['delivery time 2']=X_CES['Delivery time'].map(deliveryTimeMap)
X_CES=X_CES.drop(['Delivery time'],axis=1)

c='delivery time 2'
le = preprocessing.LabelEncoder()
le = le.fit(X_CES[c])
X_CES[c] = le.transform(X_CES[c])

X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_CES,Y_CES)

model=svm.SVC(gamma='auto')
model.fit(X_TRAIN,Y_TRAIN)

wynik=model.score(X_TEST,Y_TEST)

print('Skutecznosc=>'+str(wynik))

'''
Krzywa roc - zaleznosc pomiedzy przykladami dobrze i zle sklasyfikowanymi.
Im bardziej stroma tym lepiej.
'''
Y_PRED_PROB=model.predict(X_TEST)
fpr,tpr,_=met.roc_curve(Y_TEST,Y_PRED_PROB)
auc=met.roc_auc_score(Y_TEST,Y_PRED_PROB)

plt.plot(fpr,tpr,label='data1,auc='+str(auc))
plt.legend(loc=4)
plt.show()

#kkrotna - walidacja krzyzowa MODUL3 lekcja 6
#dzielimy zbior na k podzbiorow, jedna czesc test,reszta trening
#uzyskujemy k wynikow modelu,
#nasza skutecznosc to srednia
model=svm.SVC(gamma='auto')
scores=ms.cross_val_score(model,X_CES,Y_CES,cv=10) #cv- lista podzbiorow
wynik_k=scores.mean()

print(wynik_k)