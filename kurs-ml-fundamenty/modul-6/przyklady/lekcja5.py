import pandas
df = pandas.read_csv("caesarian.csv", sep=",", header=0)
df.head()

X = df.iloc[:, 0:5]
Y = df.iloc[:, 5]

delivery_time_map = {
    0: 'timely',
    1: 'premature',
    2: 'latecomer'
}
X['delivery time 2'] = X['Delivery time'].map(delivery_time_map)
X = X.drop(['Delivery time'], axis=1)
X.head()

X = pandas.get_dummies(X)
X.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

from sklearn import svm

model = svm.SVC(gamma='auto')
model.fit(X_train, y_train)

model.score(X_test, y_test)

import matplotlib.pyplot as plt
from sklearn import metrics

y_pred_prob = model.predict(X_test)
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_prob)
auc = metrics.roc_auc_score(y_test, y_pred_prob)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

from sklearn.model_selection import cross_val_score

model = svm.SVC(gamma='auto')

scores = cross_val_score(model, X, Y, cv=10)
print(scores.mean())