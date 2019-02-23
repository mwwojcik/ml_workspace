import pandas as pd
import opennlptagger as tagger
from narzedzia import daj_iloczyn_kartezjanski


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

wynik=daj_iloczyn_kartezjanski(OPERATORY_POROWNANIA_STOPNIOWANE,OPERATORY_STOPNIOWANIA)



# dodaje operatory podstawowe
wynik = wynik.append(OPERATORY_POROWNANIA_PODSTAWOWE,ignore_index=True)

zaprzeczenia=daj_iloczyn_kartezjanski(OPERATORY_ZAPRZECZENIA,wynik)

wynik=wynik.append(zaprzeczenia,ignore_index=True)

def utworz_warunki():
    otagowane=pd.Series(tagger.taguj('xxx','porowanie_OL')+' '+wynik.apply(lambda x:tagger.taguj(x,'operator_porownania'))+' '+tagger.taguj('xxx','porowanie_OP'))
    return otagowane
