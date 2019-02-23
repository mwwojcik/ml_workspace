import opennlptagger as tagger
import pandas as pd
from narzedzia import daj_trojwymiarowy_iloczyn_kartezjanski

START_REGULY=pd.Series(['jeśli','gdy','jeżeli'])

KONIEC_REGULY=pd.Series(['wtedy','to'])

def utworz_reguly(aFrazyWarunkow:pd.Series):

    wynik_mnozenia=daj_trojwymiarowy_iloczyn_kartezjanski(START_REGULY,aFrazyWarunkow,KONIEC_REGULY)

    # lacze kolumny
    wynik = pd.Series(tagger.taguj(wynik_mnozenia['a'],'regula_start')+' '+wynik_mnozenia['b']+' '+tagger.taguj(wynik_mnozenia['c'],'regula_stop')+' .')
    #wynik = pd.Series(
     #   tagger.taguj(wynik_mnozenia['a'], 'regula_start') + ' ' + wynik_mnozenia['b']+' .')
    return wynik