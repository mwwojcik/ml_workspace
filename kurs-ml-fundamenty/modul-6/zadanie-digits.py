# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
img_nrows, img_ncols = 28, 28

'''
Zwraca parę (etykieta,WEKTOR_PIKSELI[0...n])
Uwaga: przekształcenie Series->Array
'''
def dajEtykieteIWektorSurowy(wiersz_z_etykieta):
    return wiersz_z_etykieta.iloc[0], wiersz_z_etykieta.iloc[1:].values

def przeksztalcWektorNaObrazek(wiersz_bez_etykiety):
    return wiersz_bez_etykiety.reshape((img_nrows, img_ncols))

#img - macierz pixeli o wymiarach 28x28 reprezentujacych obrazek
def wyswietlObrazek(img):
    # Display the first digit
    plt.figure(1, figsize=(3, 3))
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()

'''
*****************************************************************
********************** METODY K-MEANS ***************************
*****************************************************************

'''
'''
Dokonuje losowego wyogdrębnienia k-liczby centroidów.
Etykiety są pomijane.
'''
def wylosujCentroidy(wektory_etykietowane,k):
    wynik=random.sample(wektory_etykietowane,k)
    wynik_bez_etykiety=[x[1] for x in wynik]
    return wynik_bez_etykiety

def policzSumeDlaKlastra(labelled_cluster):

    # assumes len(cluster) > 0
    #print("========>"+str(labelled_cluster))
    sum_ = labelled_cluster[0][1].copy()
    for (label,vector) in labelled_cluster[1:]:
        #print("vector=>"+str(vector))
        sum_ += vector
    return sum_

def policzSredniaDlaKlastra(labelled_cluster):
    if len(labelled_cluster)==0:
        print ("Pusty klaster.BLAD!")
    """
    compute the mean (i.e. centroid at the middle)
    of a list of vectors (a cluster):
    take the sum and then divide by the size of the cluster.
    """
    sum_of_points = policzSumeDlaKlastra(labelled_cluster)
    mean_of_points = sum_of_points * (1.0 / len(labelled_cluster))
    return mean_of_points

def form_clusters(labelled_data, unlabelled_centroids):
    """
    given some data and centroids for the data, allocate each
    datapoint to its closest centroid. This forms clusters.
    """
    # enumerate because centroids are arrays which are unhashable
    centroids_indices = range(len(unlabelled_centroids))

    # initialize an empty list for each centroid. The list will
    # contain all the datapoints that are closer to that centroid
    # than to any other. That list is the cluster of that centroid.
    print("----FORM_CLUSTERS----")
    clusters = {c: [] for c in centroids_indices}

    for (label,Xi) in labelled_data:
        # for each datapoint, pick the closest centroid.
        smallest_distance = float("inf")
        for cj_index in centroids_indices:
            cj = unlabelled_centroids[cj_index]
            distance = np.linalg.norm(Xi - cj)
            if distance < smallest_distance:
                closest_centroid_index = cj_index
                smallest_distance = distance
        # allocate that datapoint to the cluster of that centroid.
        clusters[closest_centroid_index].append((label,Xi))

    #for (lab,val) in enumerate(clusters):
     #   print(str(lab)+"=>"+str(val))

    return clusters.values()

def move_centroids(labelled_clusters):
    """
    returns list of mean centroids corresponding to clusters.
    """
    print("----MOVE_CENTROIDS----")
    new_centroids = []
    for cluster in labelled_clusters:
        new_centroids.append(policzSredniaDlaKlastra(cluster))
    return new_centroids

def repeat_until_convergence(labelled_data, labelled_clusters, unlabelled_centroids):
    """
    form clusters around centroids, then keep moving the centroids
    until the moves are no longer significant.
    """
    print("----repeat_until_convergence----")
    previous_max_difference = 0
    while True:
        unlabelled_old_centroids = unlabelled_centroids
        unlabelled_centroids = move_centroids(labelled_clusters)
        labelled_clusters = form_clusters(labelled_data, unlabelled_centroids)
        # keep old_clusters and clusters so we can get the maximum difference
        # between centroid positions every time.
        differences = map(lambda a, b: np.linalg.norm(a-b),unlabelled_old_centroids,unlabelled_centroids)
        max_difference = max(differences)
        difference_change = abs((max_difference-previous_max_difference)/np.mean([previous_max_difference,max_difference])) * 100
        previous_max_difference = max_difference
        # difference change is nan once the list of differences is all zeroes.
        if np.isnan(difference_change):
            break
    return labelled_clusters, unlabelled_centroids
def assign_labels_to_centroids(clusters, centroids):
    """
    Assigns a digit label to each centroid. Note: This function
     depends on clusters and centroids being in the same order.
    """
    labelled_centroids = []
    for i in range(len(clusters)):
        labels = map(lambda x: x[0], clusters[i])
        # pick the most common label
        most_common = max(set(labels), key=labels.count)
        centroid = (most_common, centroids[i])
        labelled_centroids.append(centroid)
    return labelled_centroids

def cluster(labelled_data, k):
    """
    runs k-means clustering on the data.
    """
    centroids = wylosujCentroidy(labelled_data, k)
    clusters = form_clusters(labelled_data, centroids)
    final_clusters, final_centroids = repeat_until_convergence(labelled_data, clusters, centroids)
    return final_clusters, final_centroids
'''
*****************************************************************
*****************************************************************
*****************************************************************
'''

def classify_digit(digit, labelled_centroids):
    """
    given an unlabelled digit represented by a vector and a list of
    labelled centroids [(label,vector)], determine closest centroid
    and thus classify the digit.
    """
    mindistance = float("inf")
    for (label, centroid) in labelled_centroids:
        distance = np.linalg.norm(centroid - digit)
        if distance < mindistance:
            mindistance = distance
            closest_centroid_label = label
    return closest_centroid_label

def get_error_rate(labelled_digits,labelled_centroids):
    """
    classifies a list of labelled digits. returns the error rate.
    """
    classified_incorrect = 0
    for (label,digit) in labelled_digits:
        classified_label =classify_digit(digit, labelled_centroids)
        if classified_label != label:
            classified_incorrect +=1
    error_rate = classified_incorrect / float(len(digits))
    return error_rate

#Load the digits dataset
#digitsA = datasets.load_digits()
#digits=df.iloc[:,1:785]

df=pd.read_csv('dane/digits_train.csv',sep=",",header=0)

df_pary_etykieta_wektor=df.apply(lambda x:dajEtykieteIWektorSurowy(x))

wektory_poetykietowane=df_pary_etykieta_wektor.values.tolist()
centroidy=wylosujCentroidy(wektory_poetykietowane,10)
print(centroidy)


k = 16
clusters, centroids = cluster(wektory_poetykietowane, k)
#labelled_centroids = assign_labels_to_centroids(clusters, centroids)

#for (label,digit) in labelled_centroids:
    #display_digit(digit, labeled=False, title=label)


#kazdy wiersz df przeksztalc na pare (etykieta,WEKTOR_PIKSELI)
#wektory_poetykietowane=[]

#for index, row in df.iterrows():
#    wektory_poetykietowane.append(dajEtykieteIWektorSurowy(row))

#print(wektory_poetykietowane[0])

#centroidy=wylosujCentroidy(wektory_poetykietowane,10)

#print(centroidy)

#wyswietlObrazek(przeksztalcWektorNaObrazek(wiersz_etykietowany[1]))

