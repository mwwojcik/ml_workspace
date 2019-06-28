import pandas as pd
import sklearn.model_selection as ms
import sklearn.metrics as metr
import sklearn.linear_model as linear_model

def zamienDaneNieliczboweBezZmianyWymiarow(aDF):
    #print(aDF['State'].unique())
    stateMap={
        'New York':1,
        'California':2,
        'Florida':3
    }
    aDF['State']=aDF['State'].map(stateMap)



#wczytanie danych
df=pd.read_csv('dane/zadanie-domowe-startupy.csv',header=0,sep=',')
#**** przygotowanie danych
zamienDaneNieliczboweBezZmianyWymiarow(df)

X_STARTUP=df.iloc[:,0:4]
Y_STARTUP=df.iloc[:,4]

#**** podzial na dane treningowe i testowe
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_STARTUP,Y_STARTUP)

#**** przygotowanie modelu
regr=linear_model.LinearRegression()
#*** trening modelu
regr.fit(X_TRAIN,Y_TRAIN)

#**** predykcja na danych tekstowych
Y_PRED=regr.predict(X_TEST)

print('Cechy=>{}'.format(df.columns.values))
print('Wspolczynniki=>{}'.format(regr.coef_))
print('Wyraz wolny b=>{}'.format(regr.intercept_))
print('Blad sredniokwadratowy=>{}'.format(metr.mean_squared_error(Y_TEST,Y_PRED)))
print('Wspolczynnik determinacji (R^2)=>{}'.format(regr.score(X_TRAIN,Y_TRAIN)))

'''
******************************************************************
********************* WYJSCIE ************************************
Cechy=>['R&D Spend' 'Administration' 'Marketing Spend' 'State' 'Profit']
Wspolczynniki=>[ 7.76155623e-01 -9.74809216e-03  3.29538934e-02  1.72697224e+03]
Wyraz wolny b=>45136.85190274252
Blad sredniokwadratowy=>191395018.40573347
Wspolczynnik determinacji (R^2)=>0.9680842676814594
*******************************************************************
'''