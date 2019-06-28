import pandas as pd
import sklearn.model_selection as ms
import sklearn.metrics as metr
import sklearn.linear_model as linear_model

def zamienDaneNieliczboweZeZmianaWymiarow(aDF):
    pDf=pd.get_dummies(aDF)
    return pDf

#wczytanie danych
df=pd.read_csv('dane/zadanie-domowe-startupy.csv',header=0,sep=',')
#**** przygotowanie danych
df=zamienDaneNieliczboweZeZmianaWymiarow(df)

print(df.head())
X_STARTUP=df[['R&D Spend','Administration', 'Marketing Spend','State_California', 'State_Florida']]
Y_STARTUP=df[['Profit']]

#**** podzial na dane treningowe i testowe
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_STARTUP,Y_STARTUP)

#**** przygotowanie modelu
regr=linear_model.LinearRegression()
#*** trening modelu
regr.fit(X_TRAIN,Y_TRAIN)

#**** predykcja na danych tekstowych
Y_PRED=regr.predict(X_TEST)

print('Cechy=>{}'.format(X_STARTUP.columns.values))
print('Wspolczynniki=>{}'.format(regr.coef_))
print('Wyraz wolny b=>{}'.format(regr.intercept_))
print('Blad sredniokwadratowy=>{}'.format(metr.mean_squared_error(Y_TEST,Y_PRED)))
print('Wspolczynnik determinacji (R^2)=>{}'.format(regr.score(X_TRAIN,Y_TRAIN)))

'''
******************************************************************
********************* WYJSCIE ************************************
Cechy=>['R&D Spend' 'Administration' 'Marketing Spend' 'State_California' 'State_Florida']
Wspolczynniki=>[[7.86929418e-01 7.47221918e-03 2.60564187e-02 2.72978493e+03 2.17399129e+03]]
Wyraz wolny b=>[46024.74620307]
Blad sredniokwadratowy=>145365032.5685535
Wspolczynnik determinacji (R^2)=>0.9583282803738061

###### 
Cechy=>['R&D Spend' 'Administration' 'Marketing Spend' 'State_California' 'State_Florida' 'State_New York']
Wspolczynniki=>[[ 7.61776033e-01  3.66124717e-02  2.51873958e-02  3.15311841e+02
   1.99569114e+02 -5.14880954e+02]]
Wyraz wolny b=>[47610.57213992]
Blad sredniokwadratowy=>183424088.01281166
Wspolczynnik determinacji (R^2)=>0.9644192489828582
*******************************************************************
'''