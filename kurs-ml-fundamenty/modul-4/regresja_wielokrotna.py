import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as linear_model
import sklearn.metrics as metr

#regresja liniowa ale z analiza wielu czynnikow
def zamienDaneNieliczboweDummies(aDF):
    return pd.get_dummies(aDF)

def zamienDaneNieliczboweBezZmianyWymiarow(aDF):
    print(df['color'].unique())
    print(df['cut'].unique())

    colorMap={
        'D':7,
        'E':6,
        'F':5,
        'G':4,
        'H':3,
        'I':2,
        'J':1
    }

    cutMap={
        'Ideal':5,
        'Premium':4,
        'Very Good':3,
        'Good':2,
        'Fair':1
    }

    df['colorNumber']=df['color'].map(colorMap)
    df['cutNumber']=df['cut'].map(cutMap)

    aDFLiczbowe=aDF.drop(['cut','color'],axis=1)

    return aDFLiczbowe


#**** wczytywanie modelu
df=pd.read_csv('diamonds_multi.csv',header=0,sep=';')
#**** przygotowanie danych
df_liczbowe_dum=zamienDaneNieliczboweDummies(df)
df_liczbowe=zamienDaneNieliczboweBezZmianyWymiarow(df)

X_DIAM=df_liczbowe.iloc[:,1:]
Y_DIAM=df_liczbowe.iloc[:,0]
#**** podzial na dane treningowe i testowe
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_DIAM,Y_DIAM,random_state=1)
#**** przygotowanie modelu
regr=linear_model.LinearRegression()
#*** trening modelu
regr.fit(X_TRAIN,Y_TRAIN)

#**** predykcja na danych tekstowych
Y_PRED=regr.predict(X_TEST)

#**** wyniki
#y=a1x1+a2x2+a3x3 ... + b
print('Wspolczynnik a='+str(regr.coef_))
print('Wyraz wolny b='+str(regr.intercept_))
print('Blad sredniokwadratowy='+str(metr.mean_squared_error(Y_TEST,Y_PRED)))
print('Wspolczynnik R^2='+str(regr.score(X_TRAIN,Y_TRAIN))) #R^2=1 - wynik idealny


#plt.scatter(X_TRAIN['x'],Y_TRAIN)
#plt.xlabel('carat')
#plt.ylabel('price')
#rysujemy funkcje liniowa
#plt.scatter(X_TEST,Y_TEST,color='red')
#plt.show()
