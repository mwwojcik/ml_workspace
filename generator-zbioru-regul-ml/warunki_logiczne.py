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

OPERATORY_LOGICZNE=pd.Series(["lub","oraz","i"])

def utworz_warunki_laczone(warunki_pojedyncze:pd.Series):
    warunki_lewa_strona=warunki_pojedyncze.copy()
    warunki_prawa_strona=warunki_pojedyncze.copy()
    operatory_logiczne_otagowane=pd.Series(OPERATORY_LOGICZNE.apply(lambda x:tagger.taguj(x,'operator_logiczny')))
    wynik_mnozenia=narzedzia.wylicz_iloczyn_kartezjanski([warunki_lewa_strona, operatory_logiczne_otagowane, warunki_prawa_strona],['a','b','c'])
    #splaszczam i wybieram losowo n elementow gdzie n to dlugosc wektora WE
    return pd.Series(wynik_mnozenia['a']+' '+wynik_mnozenia['b']+' '+wynik_mnozenia['c']).sample(n=len(warunki_pojedyncze))

def utworz_warunki():
    warunki_pojedyncze_otagowane=pd.Series(tagger.taguj('xxx','porowanie_OL')+' '+wynik.apply(lambda x:tagger.taguj(x,'operator_porownania'))+' '+tagger.taguj('xxx','porowanie_OP'))
    #return warunki_pojedyncze_otagowane
    warunki_laczone_otagowane=utworz_warunki_laczone(warunki_pojedyncze_otagowane)
    return warunki_pojedyncze_otagowane.append(warunki_laczone_otagowane)
