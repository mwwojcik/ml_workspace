import sys
sys.path.insert(0, '../narzedzia/')
from raportowanie import raport,printdf,headdf
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import cluster
from sklearn.metrics import silhouette_score

import pandas as pd
df=pd.read_csv('dane/Mall_Customers.csv',sep=',',header=0)
printdf(df)

df.plot.scatter(x='Spending Score (1-100)',y='Annual Income (k$)')
plt.show()

#na diagramie widac potencjalny podzial na 5 grup
df=df.drop(['CustomerID'],axis=1)

c='Gender'
le = preprocessing.LabelEncoder()
le = le.fit(df[c])
df[c] = le.transform(df[c])

kmeans=cluster.KMeans(n_clusters=6,init='k-means++').fit(df)

print(kmeans.labels_)
plt.scatter(x=df['Spending Score (1-100)'],y=df['Annual Income (k$)'],c=kmeans.labels_,cmap='rainbow')
plt.colorbar()
plt.show()

wynik=kmeans.predict([[40,130,90,1]]) #40 lat, zarabia dosyc duzo bo 130,wydaje 90,mezczyzna
print(wynik)
#[4] -> przypisano do klasy 4
sylwetka=silhouette_score(df,kmeans.labels_)
print(sylwetka)

#sprawdzamy czy liczba klastrow jest najbardziej optymalna
#trzeba uwzglednic ze poki co uwzglednilismy tylko dwie wartosci

result=[]
num_clusters=[]

for i in range(2,14):
    kmeans=cluster.KMeans(n_clusters=i).fit(df)
    s=silhouette_score(df,kmeans.labels_)
    result.append(s)
    num_clusters.append(i)
plt.scatter(x=num_clusters,y=result)
plt.show()
#optymalna liczba klastrow dla wszystkich cech to 6
