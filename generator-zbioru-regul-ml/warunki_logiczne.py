import pandas as pd
import opennlptagger as tagger
from narzedzia import podaj_dwuwymiarowy_iloczyn_kartezjanski
import narzedzia


OPERATORY_ZAPRZECZENIA=pd.Series(['nie'])

OPERATORY_POROWNANIA_PODSTAWOWE = pd.Series(['jest równy','jest większy lub równy', 'jest mniejszy lub równa','jest równa','jest większa lub równa', 'jest mniejsza lub równa','jest równe','jest większe lub równe', 'jest mniejsze lub równe'])

OPERATORY_POROWNANIA_STOPNIOWANE = pd.Series(['jest większy', 'jest mniejszy', 'jest różny','jest większa', 'jest mniejsza', 'jest różna','jest większe', 'jest mniejsze', 'jest różne'])
OPERATORY_STOPNIOWANIA = pd.Series(['niż', 'od'])
operatory_stopniowane=podaj_dwuwymiarowy_iloczyn_kartezjanski(OPERATORY_POROWNANIA_STOPNIOWANE, OPERATORY_STOPNIOWANIA)
#splaszczenie
wynik=pd.Series(operatory_stopniowane['a']+' '+operatory_stopniowane['b'])



# dodaje operatory podstawowe
wynik = wynik.append(OPERATORY_POROWNANIA_PODSTAWOWE,ignore_index=True)

zaprzeczenia=podaj_dwuwymiarowy_iloczyn_kartezjanski(OPERATORY_ZAPRZECZENIA, wynik)
#splaszczenie
zaprzeczenia_wynik=pd.Series(zaprzeczenia['a']+' '+zaprzeczenia['b'])

wynik=wynik.append(zaprzeczenia_wynik,ignore_index=True)

print(str(wynik))

OPERATORY_LOGICZNE=pd.Series(["lub","oraz","i"])

def utworz_warunki_czy_null():
    OPERATORY_CZY_NULL=pd.Series([   "jest puste","nie jest puste","jest niepuste"
                                     ,"ma wartość","nie ma wartości"
                                     ,"jest określone","nie jest określone"
                                     ,"jest doprecyzowane", "nie jest doprecyzowane"
                                     ,"zostało wprowadzone","nie zostało wprowadzone"
                                     ,"ma wartość","nie ma wartości"
                                     , "zostało podane", "nie zostało podane"
                                  ])
    return pd.Series(tagger.taguj('xxx','porowanie_czy_null_OP')+' '+OPERATORY_CZY_NULL.apply(lambda x:tagger.taguj(x,'operator_porownania_czy_null')))

def utworz_warunki_laczone(warunki_pojedyncze:pd.Series):
    warunki_lewa_strona=warunki_pojedyncze.copy()
    warunki_prawa_strona=warunki_pojedyncze.copy()
    operatory_logiczne_otagowane=pd.Series(OPERATORY_LOGICZNE.apply(lambda x:tagger.taguj(x,'operator_logiczny')))
    wynik_mnozenia=narzedzia.wylicz_iloczyn_kartezjanski([warunki_lewa_strona, operatory_logiczne_otagowane, warunki_prawa_strona],['a','b','c'])
    #splaszczam i wybieram losowo n elementow gdzie n to dlugosc wektora WE
    return pd.Series(wynik_mnozenia['a']+' '+wynik_mnozenia['b']+' '+wynik_mnozenia['c']).sample(n=25*len(warunki_pojedyncze))

def utworz_warunki():
    warunki_pojedyncze_otagowane=pd.Series(tagger.taguj('xxx','porowanie_OL')+' '+wynik.apply(lambda x:tagger.taguj(x,'operator_porownania'))+' '+tagger.taguj('xxx','porowanie_OP'))
    print("warunki_pojedyncze_otagowane(ilosc_elem)"+str(len(warunki_pojedyncze_otagowane)))
    #return warunki_pojedyncze_otagowane
    warunki_laczone_otagowane=utworz_warunki_laczone(warunki_pojedyncze_otagowane)
    print("warunki_laczone_otagowane(ilosc_elem)" + str(len(warunki_laczone_otagowane)))
    warunki_czy_null_otagowane=utworz_warunki_czy_null()
    print("warunki_czy_null_otagowane(ilosc_elem)" + str(len(warunki_czy_null_otagowane)))
    warunki_czy_null_laczone = utworz_warunki_laczone(warunki_czy_null_otagowane)
    print("warunki_czy_null_laczone(ilosc_elem)" + str(len(warunki_czy_null_laczone)))
    warunki_razem=warunki_pojedyncze_otagowane.append(warunki_laczone_otagowane).append(warunki_czy_null_otagowane).append(warunki_czy_null_laczone)
    print("warunki_razem(ilosc_elem)" + str(len(warunki_razem)))
    return warunki_razem

