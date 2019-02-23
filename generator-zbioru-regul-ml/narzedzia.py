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

def daj_dwuwymiarowy_iloczyn_kartezjanski(zbiorA:pd.Series,zbiorB:pd.Series):
    # tworze indeks dwuwymiarowy
    indeks_dwuwymiarowy = pd.MultiIndex.from_product([zbiorA, zbiorB],
                                                     names=["a", "b"])
    wynik_mnozenia = pd.DataFrame(index=indeks_dwuwymiarowy).reset_index()
    # lacze kolumny
    #wynik = pd.Series(wynik_mnozenia['a'] + ' ' + wynik_mnozenia['b'])
    return wynik_mnozenia

def daj_trojwymiarowy_iloczyn_kartezjanski(zbiorA:pd.Series,zbiorB:pd.Series,zbiorC:pd.Series):
    # tworze indeks dwuwymiarowy
    indeks_trojwymiarowy = pd.MultiIndex.from_product([zbiorA, zbiorB,zbiorC],
                                                     names=["a", "b","c"])
    wynik = pd.DataFrame(index=indeks_trojwymiarowy).reset_index()
    return wynik
