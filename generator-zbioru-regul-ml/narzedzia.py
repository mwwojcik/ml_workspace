import pandas as pd
'''
def daj_iloczyn_kartezjanski(zbiorA:pd.Series,zbiorB:pd.Series):
    # tworze indeks dwuwymiarowy
    indeks_dwuwymiarowy = pd.MultiIndex.from_product([zbiorA, zbiorB],
                                                     names=["a", "b"])
    wynik_mnozenia = pd.DataFrame(index=indeks_dwuwymiarowy).reset_index()
    # lacze kolumny
    wynik = pd.Series(wynik_mnozenia['a'] + ' ' + wynik_mnozenia['b'])
    return wynik
'''

def podaj_dwuwymiarowy_iloczyn_kartezjanski(zbiorA:pd.Series, zbiorB:pd.Series):
    # tworze indeks dwuwymiarowy
    indeks_dwuwymiarowy = pd.MultiIndex.from_product([zbiorA, zbiorB],
                                                     names=["a", "b"])
    wynik_mnozenia = pd.DataFrame(index=indeks_dwuwymiarowy).reset_index()
    # lacze kolumny
    #wynik = pd.Series(wynik_mnozenia['a'] + ' ' + wynik_mnozenia['b'])
    return wynik_mnozenia

def podaj_trojwymiarowy_iloczyn_kartezjanski(zbiorA:pd.Series, zbiorB:pd.Series, zbiorC:pd.Series):
    # tworze indeks dwuwymiarowy
    indeks_trojwymiarowy = pd.MultiIndex.from_product([zbiorA, zbiorB,zbiorC],
                                                     names=["a", "b","c"])
    wynik = pd.DataFrame(index=indeks_trojwymiarowy).reset_index()
    return wynik

'''
zbiorA:pd.Series, zbiorB:pd.Series, zbiorC:pd.Series
names=["a", "b","c"])
'''
def wylicz_iloczyn_kartezjanski(grupa_serii:list,nazwy_kolumn:list):
    # tworze indeks dwuwymiarowy
    indeks = pd.MultiIndex.from_product(grupa_serii,names=nazwy_kolumn)
    wynik = pd.DataFrame(index=indeks).reset_index()
    return wynik

'''
def wylicz_iloczyn_kartezjanski_dla_macierzy(zbiorA:pd.DataFrame,zbiorB:pd.DataFrame,nazwy_kolumn:list):
    indeks_macierzy=pd.MultiIndex.from_product([zbiorA,zbiorB],names=nazwy_kolumn)
    wynik=pd.DataFrame(indeks=indeks_macierzy).reset_index()
    return wynik

def wylicz_iloczyn_kartezjanski_macierzxseria(zbiorA:pd.DataFrame,zbiorB:pd.Series,nazwy_kolumn:list):
    return wylicz_iloczyn_kartezjanski_dla_macierzy(zbiorA,pd.DataFrame(zbiorB),nazwy_kolumn)

def wylicz_iloczyn_kartezjanski_seriaxseria(zbiorA:pd.Series,zbiorB:pd.Series,nazwy_kolumn:list):
    return wylicz_iloczyn_kartezjanski_dla_macierzy(pd.DataFrame(zbiorA),pd.DataFrame(zbiorB),nazwy_kolumn)

'''