# Polynomial Regression

# Importing the libraries
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.model_selection as ms
import sklearn.linear_model as linear_model
import sklearn.metrics as metr

#**** wczytanie danych
#header=0 to znaczy że jest on na pozycji 0
df = pd.read_csv('dane/Position_Salaries.csv',header=0,sep=',')

#**** przygotowanie danych
X_SAL=df.iloc[:,1:2]
Y_SAL=df.iloc[:,2]

#**** podzial na dane treningowe i testowe
#X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=ms.train_test_split(X_SAL,Y_SAL,random_state=1,

#**** przygotowanie modelu
poly=PolynomialFeatures(degree=4)
X_POLY = poly.fit_transform(X_SAL)
#*** trening modelu
regr=linear_model.LinearRegression()
regr.fit(X_POLY,Y_SAL)

Y_PRED=regr.predict(poly.fit_transform(X_SAL))

print('Regresja wielomianowa')
print('Wspolczynniki a='+str(regr.coef_))
print('Wyraz wolny b='+str(regr.intercept_))
print('Blad sredniokwadratowy='+str(metr.mean_squared_error(Y_SAL,Y_PRED)))
print('Wspolczynnik determinacji (R^2)='+str(regr.score(poly.fit_transform(X_SAL),Y_SAL)))

#dla porownania uzyskuje wyniki z regresji prostej
#przygotowanie modelu
prosta_regr=linear_model.LinearRegression()
prosta_regr.fit(X_SAL,Y_SAL)

#predykcja
Y_PRED_PROSTA_REGR=prosta_regr.predict(X_SAL)

print('\n '
      'Zwykła regresja liniowa')
print('Wspolczynniki a='+str(prosta_regr.coef_))
print('Wyraz wolny b='+str(prosta_regr.intercept_))
print('Blad sredniokwadratowy='+str(metr.mean_squared_error(Y_SAL,Y_PRED_PROSTA_REGR)))
print('Wspolczynnik determinacji (R^2)='+str(prosta_regr.score(X_SAL,Y_SAL)))

#*** Wizualizacja wynikow

plt.subplots(2,1,figsize=(10,10))
plt.subplot(2, 1, 1)
plt.scatter(X_SAL,Y_SAL, color = 'red')
plt.plot(X_SAL,Y_PRED, color = 'blue')
plt.title(' Score (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')


plt.subplot(2, 1, 2)
plt.scatter(X_SAL,Y_SAL, color = 'red')
plt.plot(X_SAL,Y_PRED_PROSTA_REGR, color = 'blue')
plt.title('Score (Simple Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()