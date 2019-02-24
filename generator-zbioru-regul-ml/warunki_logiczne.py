import pandas as pd
import opennlptagger as tagger
from narzedzia import podaj_dwuwymiarowy_iloczyn_kartezjanski


OPERATORY_ZAPRZECZENIA=pd.Series(['nie'])

OPERATORY_POROWNANIA_PODSTAWOWE = pd.Series(['jest równy', 'jest równa', 'jest równe'
                                                , 'jest większy lub równy', "jest większa lub równa"
                                                , 'jest większe lub równe'
                                                , 'jest mniejszy lub równy', 'jest mniejsza lub równa'
                                                , 'jest mniejsze lub równe'])

OPERATORY_POROWNANIA_STOPNIOWANE = pd.Series(['jest większy', 'jest większa', 'jest większe'
                                                 , 'jest mniejszy', 'jest mniejsza', 'jest mniejsze'
                                                 , 'jest różny', 'jest różna', 'jest różne'
                                              ])
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

def utworz_warunki():
    otagowane=pd.Series(tagger.taguj('xxx','porowanie_OL')+' '+wynik.apply(lambda x:tagger.taguj(x,'operator_porownania'))+' '+tagger.taguj('xxx','porowanie_OP'))
    return otagowane
