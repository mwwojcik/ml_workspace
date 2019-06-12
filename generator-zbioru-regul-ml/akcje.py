import pandas as pd
import opennlptagger as tagger


AKCJE=pd.Series(['zgłoś błąd','zgłoś błąd walidacji','raportuj błąd','wyświetl komunikat','sprawdź regułę','sprawdzaj regułę'])

AKCJE_OTAGOWANE=pd.Series(AKCJE.apply(lambda x: tagger.taguj(x,"AKCJA")+' '+tagger.taguj('xxx','AKCJA_PARAMETR')))

def utworz_akcje():
    return AKCJE_OTAGOWANE