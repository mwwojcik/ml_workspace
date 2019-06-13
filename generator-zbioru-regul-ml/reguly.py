import opennlptagger as tagger
import akcje
import pandas as pd
import narzedzia
import random


'''
*******************************
*******************************
Początek obslugi stalych wektorow
*******************************
*******************************
'''
START_REGULY=pd.Series(['jeśli','gdy','jeżeli'])
KONIEC_REGULY=pd.Series(['wtedy','to'])
W_PRZECIWNYM_WYPADKU=pd.Series(['w przeciwnym wypadku'])
AKCJE=akcje.utworz_akcje()
'''
*******************************
*******************************
Koniec obslugi stalych wektorow
*******************************
*******************************
'''


def utworz_reguly(aFrazyWarunkow:pd.Series):

    WYNIK_MNOZENIA_SKLADOWYCH_REGULY=narzedzia.wylicz_iloczyn_kartezjanski([START_REGULY, aFrazyWarunkow, KONIEC_REGULY,AKCJE],['a','b','c','d'])
    # wypłaszczenie
    REGULY = pd.Series(
        tagger.taguj(WYNIK_MNOZENIA_SKLADOWYCH_REGULY['a'], 'SK_SW') + ' ' + WYNIK_MNOZENIA_SKLADOWYCH_REGULY['b'] + ' ' + tagger.taguj(
            WYNIK_MNOZENIA_SKLADOWYCH_REGULY['c'], 'SK_KW') + ' ' + WYNIK_MNOZENIA_SKLADOWYCH_REGULY['d'] +' .')

    print("Ilość rekordów w próbce przed dodaniem ELSE=>" + str(len(REGULY)))




    CZESC_ELSE_OTAGOWANA = pd.Series(tagger.taguj(W_PRZECIWNYM_WYPADKU, 'SK_SAN'))
    CZESC_ELSE_OTAGOWANA_X_AKCJE = narzedzia.wylicz_iloczyn_kartezjanski([CZESC_ELSE_OTAGOWANA, AKCJE], ['a', 'b'])
    CZESC_ELSE_OTAGOWANA_X_AKCJE_WYNIK = pd.Series(
        CZESC_ELSE_OTAGOWANA_X_AKCJE['a'] + ' ' + CZESC_ELSE_OTAGOWANA_X_AKCJE['b'])

    print("Ilość CZESC_ELSE_OTAGOWANA_X_AKCJE_WYNIK=>" + str(len(CZESC_ELSE_OTAGOWANA_X_AKCJE_WYNIK)))

    # tworze sobie kopie wektora regul by wzbogacic go o czesc ELSE
    REGULY_KOPIA = pd.Series(
        tagger.taguj(WYNIK_MNOZENIA_SKLADOWYCH_REGULY['a'], 'SK_SW') + ' ' + WYNIK_MNOZENIA_SKLADOWYCH_REGULY[
            'b'] + ' ' + tagger.taguj(
            WYNIK_MNOZENIA_SKLADOWYCH_REGULY['c'], 'SK_KW') + ' ' + WYNIK_MNOZENIA_SKLADOWYCH_REGULY['d'] + ' ')
    print("Ilość REGULY_KOPIA=>" + str(len(REGULY_KOPIA)))

    REGULY_KOPIA_X_CZESC_ELSE_OTAGOWANA_X_AKCJE = narzedzia.wylicz_iloczyn_kartezjanski([REGULY_KOPIA, CZESC_ELSE_OTAGOWANA_X_AKCJE_WYNIK],['a', 'b'])
    REGULY_KOPIA_X_Z_CZESCIA_ELSE_WYNIK = pd.Series(REGULY_KOPIA_X_CZESC_ELSE_OTAGOWANA_X_AKCJE['a'] + ' ' + REGULY_KOPIA_X_CZESC_ELSE_OTAGOWANA_X_AKCJE['b'] + ' .')
    print("Ilość REGULY_KOPIA_X_Z_CZESCIA_ELSE_WYNIK=>" + str(len(REGULY_KOPIA_X_Z_CZESCIA_ELSE_WYNIK)))

    REGULY_POLACZONE=REGULY.append(REGULY_KOPIA_X_Z_CZESCIA_ELSE_WYNIK, ignore_index=True)
    print("Ilość REGULY_POLACZONE=>" + str(len(REGULY_POLACZONE)))
    return REGULY_POLACZONE
'''
   



    



    wynik_laczony=wynik.append(wynik_w_przeciwny_wyplaszczony.sample(30000), ignore_index=True)
'''
    #print("Ilość rekordów w próbce=>" + str(len(wynik)))
    #return wynik_laczony
