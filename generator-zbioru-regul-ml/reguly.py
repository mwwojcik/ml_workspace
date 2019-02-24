import opennlptagger as tagger
import akcje
import pandas as pd
import narzedzia

START_REGULY=pd.Series(['jeśli','gdy','jeżeli'])

KONIEC_REGULY=pd.Series(['wtedy','to'])

def utworz_reguly(aFrazyWarunkow:pd.Series):

    AKCJE=akcje.utworz_akcje()

    wynik_mnozenia=narzedzia.wylicz_iloczyn_kartezjanski([START_REGULY, aFrazyWarunkow, KONIEC_REGULY,AKCJE],['a','b','c','d'])
    # wypłaszczenie
    wynik = pd.Series(tagger.taguj(wynik_mnozenia['a'],'regula_start')+' '+wynik_mnozenia['b']+' '+tagger.taguj(wynik_mnozenia['c'],'regula_stop')+' '+wynik_mnozenia['d']+' .')


    return wynik