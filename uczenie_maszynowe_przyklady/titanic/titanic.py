import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dane.obsluga_danych as dane;
from sklearn import preprocessing

data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')




sns.barplot(x="Embarked", y="Survived", hue="Sex", data=data_train);
plt.show()

sns.boxplot(x="Parch", y="Survived", hue="Sex", data=data_train, palette="PRGn");
sns.despine(offset=10, trim=True)
plt.show()

sns.pointplot(x="Pclass", y="Survived", hue="Sex", data=data_train,
              palette={"male": "blue", "female": "pink"},
              markers=["*", "o"], linestyles=["-", "--"]);
plt.show()


# Age - cecha pod wzgledem waznosci. Zeby uniknac przeuczenia
# odbywa sie grupowanie
def simplify_ages(df):
    #obsluga wartosci NAN - wstaw wartosc -0,5
    df.Age = df.Age.fillna(-0.5)
    bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
    #dyskredyzacja danych kazda wartosc liczbowa przyporzadkujemy do kategorii
    categories = pd.cut(df.Age, bins, labels=group_names)
    df.Age = categories
    return df


def simplify_cabins(df):
    #dla null podstaw N
    df.Cabin = df.Cabin.fillna('N')
    #dla itego elementu wytnij pierwsza litere i podstaw np C10=>C - nie interesuje nas numer
    df.Cabin = df.Cabin.apply(lambda x: x[0])
    return df


def simplify_fares(df):
    df.Fare = df.Fare.fillna(-0.5)
   #ponownie dyskretyzacja
    bins = (-1, 0, 8, 15, 31, 1000)
    group_names = ['Unknown', '1_quartile', '2_quartile', '3_quartile', '4_quartile']
    categories = pd.cut(df.Fare, bins, labels=group_names)
    df.Fare = categories
    return df


def format_name(df):
    #splitujemy i wybieramy pierwsza czesc z imienia - dodajemy cech
    df['Lname'] = df.Name.apply(lambda x: x.split(' ')[0])
    #plitujemy i drugi czlon wrzucamy jako nowa ceche Miss, Mrs, Mr... itd
    df['NamePrefix'] = df.Name.apply(lambda x: x.split(' ')[1])
    return df


def drop_features(df):
    #pozbywamy sie cech nieistotnych
    return df.drop(['Ticket', 'Name', 'Embarked'], axis=1)


def transform_features(df):
    df = simplify_ages(df)
    df = simplify_cabins(df)
    df = simplify_fares(df)
    df = format_name(df)
    df = drop_features(df)
    return df


def encode_features(df_train, df_test):
    features = ['Fare', 'Cabin', 'Age', 'Sex', 'Lname', 'NamePrefix']
    df_combined = pd.concat([df_train[features], df_test[features]])

    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_combined[feature])
        df_train[feature] = le.transform(df_train[feature])
        df_test[feature] = le.transform(df_test[feature])
    return df_train, df_test

#wykonujemy obrobke danych dla zbioru trenowanego i testowanego
data_train = transform_features(data_train)
data_test = transform_features(data_test)
print(data_train.head())
#dane.drukujDaneDataSeta(data_train)


#sns.barplot(x="Age", y="Survived", hue="Sex", data=data_train);
#plt.show()

#sns.barplot(x="Cabin", y="Survived", hue="Sex", data=data_train);
#plt.show()

# The last part of the preprocessing phase is to normalize labels.
# The LabelEncoder in Scikit-learn will convert each unique string value into a number, making out data more flexible for various algorithms.
encode_features(data_train,data_test)


