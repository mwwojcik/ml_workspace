import sys
sys.path.insert(0, '../narzedzia/')
sys.path.insert(1, './wspolne/')

from raportowanie import raport,printdf,headdf
from wspolne.monitoring import  raportujParametryUczenia
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection as ms
import sklearn.tree as tree
import sklearn.metrics as met

def przeksztalcajCecheAge(aDF):
    # obsluga wartosci NAN - wstaw wartosc -0,5
    aDF.Age = aDF.Age.fillna(-0.5)
    progi = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    nazwy_kategorii = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
    # kategoryzacja danych kazda wartosc liczbowa przyporzadkujemy do kategorii
    kategorie_AGE = pd.cut(aDF.Age, progi, labels=nazwy_kategorii)
    aDF.Age = kategorie_AGE
    return aDF

def przeksztalcajCecheFare(aDF):
    aDF.Fare = aDF.Fare.fillna(-0.5)
   #ponownie dyskretyzacja
    progi = (-1, 0, 8, 15, 31, 1000)
    nazwy_kategorii = ['Unknown', '1_quartile', '2_quartile', '3_quartile', '4_quartile']
    kategorie_Fare = pd.cut(aDF.Fare, progi, labels=nazwy_kategorii)
    aDF.Fare = kategorie_Fare
    return aDF

def przeksztalcajCecheEmbarked(aDF):
    #przy niezdefiniowanych wzmacniam najczestsza S
    aDF.Embarked=aDF.Embarked.fillna('S')
    return aDF

def usunNiepotrzebneKolumny(aDF):
    # pozbywamy sie cech nieistotnych
    return aDF.drop(['Ticket', 'Name', 'Cabin','PassengerId'], axis=1)
def wyodrebnijCecheFamilySize(aDF):
    aDF['FamilySize'] = aDF['Parch'] + aDF['SibSp']
    return aDF.drop(['Parch','SibSp'],axis=1)

def dokonajPrzeksztalcenDanych(aDF):
    aDF=przeksztalcajCecheAge(aDF)
    aDF=usunNiepotrzebneKolumny(aDF)
    aDF=przeksztalcajCecheFare(aDF)
    aDF=przeksztalcajCecheEmbarked(aDF)
    aDF=wyodrebnijCecheFamilySize(aDF)
    return aDF

def kodujNaWartosciLiczbowe(aDF):
    nazwyCech = ['Fare', 'Age', 'Sex','Embarked']

    for c in nazwyCech:
        le = preprocessing.LabelEncoder()
        le = le.fit(aDF[c])
        aDF[c] = le.transform(aDF[c])
    return aDF

#**** wczytanie danych
df=pd.read_csv('dane/train.csv',sep=',',header=0)
dftest=pd.read_csv('dane/test.csv',sep=',',header=0)


#**** przygotowanie danych
df=dokonajPrzeksztalcenDanych(df)
df=kodujNaWartosciLiczbowe(df)

X_TITANIC=df.iloc[:,1:8]
Y_TITANIC=df.iloc[:,0]


X_TEST_PASS_ID=dftest.PassengerId.copy()
dftest=dokonajPrzeksztalcenDanych(dftest)
dftest=kodujNaWartosciLiczbowe(dftest)


#**** podzial na zbior treningowy i testowy
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_TITANIC,Y_TITANIC,random_state=1)

#**** trening modelu
model=tree.DecisionTreeClassifier(max_depth=1.8)
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


#predykcja na potrzeby zadania
Y_PRED_SURV=model.predict(dftest)

submission = pd.DataFrame({
        "PassengerId": X_TEST_PASS_ID,
        "Survived": Y_PRED_SURV
    })
submission.to_csv('./output/submission.csv', index=False)