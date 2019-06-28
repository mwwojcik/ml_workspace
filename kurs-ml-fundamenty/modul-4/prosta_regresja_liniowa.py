import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as linear_model
import sklearn.metrics as metr

#**** wczytanie danych
#header=0 to znaczy że jest on na pozycji 0
df=pd.read_csv('dane/diamonds_single.csv',header=0,sep=';')
print(df.head())
print(df.shape)

#**** wizualizacja danych

plt.scatter(df['carat'],df['price'])
plt.xlabel('carat')
plt.ylabel('price')
plt.show()

#podzial danych na trening/testy
x_diam=df[['carat']]
y_diam=df[['price']]
Xtrain,Xtest,Ytrain,Ytest=ms.train_test_split(x_diam,y_diam,random_state=1)

#przygotowanie modelu
regr=linear_model.LinearRegression()

#trening modelu
regr.fit(Xtrain,Ytrain)

#predykcja na danych testowych
#przewidujemy wyniki dla zbioru testowego
y_pred=regr.predict(Xtest)

#wyniki
#szukamy parametrow dla y=ax+b
print('Wspolczynnik a='+str(regr.coef_))
print('Wyraz wolny b='+str(regr.intercept_))
print('Blad sredniokwadratowy='+str(metr.mean_squared_error(Ytest,y_pred)))
print('Wspolczynnik R^2='+str(regr.score(Xtrain,Ytrain))) #R^2=1 - wynik idealny

#rownanie prostej wytyczonej w procesie uczenia:
#y=7752.46574089*x-2245.2027021

plt.scatter(Xtrain,Ytrain)
plt.xlabel('carat')
plt.ylabel('price')
#rysujemy funkcje liniowa
plt.plot(Xtest,y_pred,color='red')
plt.show()