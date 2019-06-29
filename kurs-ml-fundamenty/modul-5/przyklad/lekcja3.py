import pandas
# wczytanie danych
cancer_data = pandas.read_csv(
'http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data',
                           sep= ',', header= None)

cancer_data.head()

X = cancer_data.iloc[:,1:10]
Y = cancer_data.iloc[:,0]
X2 = pandas.get_dummies(X)
X2.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X2, Y,train_size=0.9, test_size=0.1, random_state=1)

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix
y_pred = model.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
tn, fp, fn, tp

model.score(X_test, y_test)
model.score(X_train, y_train)


test_scores = []
train_scores = []
for i in range(1, 20):
    clf_gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=i)
    clf_gini.fit(X_train, y_train)
    test_scores.append(clf_gini.score(X_test, y_test))
    train_scores.append(clf_gini.score(X_train, y_train))

import matplotlib.pyplot as plt

plt.plot(test_scores, color="red")
plt.plot(train_scores)