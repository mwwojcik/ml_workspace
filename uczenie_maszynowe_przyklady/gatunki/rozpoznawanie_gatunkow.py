import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import dane.obsluga_danych as dane;

url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

dane.drukujDaneDataSeta(dataset)
dane.pokazWykresyDataSeta(dataset)

# Split-out validation dataset
array = dataset.values
#wszystkie wiersze, kolumny od 0 do 4 (bez 4)
X = array[:,0:4]
#wszystkie wiersze, tylko kolumna 4
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



# Make predictions on validation dataset
# Uruchamiamy przewidywanie na zbiorze testowym
# Zbieramy statystyki dopasowan
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

#uruchamiamy przewidywanie na pliku testowym
#dane ktore nie pojawily sie w procesie uczenia
url = "iris-predykcja.csv"
dataset_pred_csv = pandas.read_csv(url, names=names)
pred_data_arr=dataset_pred_csv.values[:,0:4]
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
print(knn.predict(pred_data_arr))
# make a prediction for an example of an out-of-sample observation
knn.predict([[6, 3, 4, 2]])



