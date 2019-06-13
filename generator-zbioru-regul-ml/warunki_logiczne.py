import pandas as pd
import opennlptagger as tagger
from narzedzia import podaj_dwuwymiarowy_iloczyn_kartezjanski
import narzedzia

'''
*******************************
*******************************
Początek obslugi wektorow stalych
*******************************
*******************************
'''
OPERATORY_ZAPRZECZENIA=pd.Series(['nie'])
OPERATORY_POROWNANIA_PODSTAWOWE = pd.Series(['jest równy' ,'jest równa', 'jest równe'])

OPERATORY_POROWNANIA_STOPNIOWANE = pd.Series(['jest większy',
                                              'jest mniejszy',
                                              'jest różny',
                                              'jest większa',
                                              'jest mniejsza',
                                              'jest różna',
                                              'jest większe',
                                              'jest mniejsze',
                                              'jest różne'])
OPERATORY_STOPNIOWANIA = pd.Series(['niż', 'od'])
OPERATORY_POSTOPNIOWANE=podaj_dwuwymiarowy_iloczyn_kartezjanski(OPERATORY_POROWNANIA_STOPNIOWANE, OPERATORY_STOPNIOWANIA)


#łączenie operatorów podstawowych z wystponiowanymi
#splaszczenie
WYNIK=pd.Series(OPERATORY_POSTOPNIOWANE['a'] + ' ' + OPERATORY_POSTOPNIOWANE['b'])
# dodaje operatory podstawowe
WYNIK = WYNIK.append(OPERATORY_POROWNANIA_PODSTAWOWE, ignore_index=True)

#
ZAPRZECZENIA=podaj_dwuwymiarowy_iloczyn_kartezjanski(OPERATORY_ZAPRZECZENIA, WYNIK)
#splaszczenie
OPERATORY_ZAPRZECZONE=pd.Series(ZAPRZECZENIA['a'] + ' ' + ZAPRZECZENIA['b'])
#dolaczenie do wyniku
WYNIK=WYNIK.append(OPERATORY_ZAPRZECZONE, ignore_index=True)

OPERATORY_LOGICZNE=pd.Series(["lub","oraz","i"])
print(str(WYNIK))

'''
*******************************
*******************************
Początek obslugi wektorow stalych
*******************************
*******************************
'''




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
    warunki_lewa_strona=warunki_pojedyncze.copy()#.sample(30)
    warunki_prawa_strona=warunki_pojedyncze.copy()#.sample(30)
    operatory_logiczne_otagowane=pd.Series(OPERATORY_LOGICZNE.apply(lambda x:tagger.taguj(x,'OPR_LOG')))
    wynik_mnozenia=narzedzia.wylicz_iloczyn_kartezjanski([warunki_lewa_strona, operatory_logiczne_otagowane, warunki_prawa_strona],['a','b','c'])
    #splaszczam i wybieram losowo n elementow gdzie n to dlugosc wektora WE
    return pd.Series(wynik_mnozenia['a']+' '+wynik_mnozenia['b']+' '+wynik_mnozenia['c'])#.sample(n=4*len(warunki_pojedyncze))

def utworz_warunki():
    warunki_pojedyncze_otagowane=pd.Series(tagger.taguj('xxx','OP_L') +' ' + WYNIK.apply(lambda x:tagger.taguj(x, 'OPR_REL')) + ' ' + tagger.taguj('xxx', 'OP_P'))
    print("warunki_pojedyncze_otagowane(ilosc_elem)"+str(len(warunki_pojedyncze_otagowane)))

    #warunki_laczone_otagowane = utworz_warunki_laczone(warunki_pojedyncze_otagowane)
    #print("warunki_laczone_otagowane(ilosc_elem)" + str(len(warunki_laczone_otagowane)))

   # warunki_razem = warunki_pojedyncze_otagowane.append(
    #    warunki_laczone_otagowane)  # .append(warunki_czy_null_otagowane).append(warunki_czy_null_laczone)
   # print("warunki_razem(ilosc_elem)" + str(len(warunki_razem)))
    return warunki_pojedyncze_otagowane


    '''
    
    warunki_czy_null_otagowane=utworz_warunki_czy_null()
    print("warunki_czy_null_otagowane(ilosc_elem)" + str(len(warunki_czy_null_otagowane)))
    warunki_czy_null_laczone = utworz_warunki_laczone(warunki_czy_null_otagowane)
    print("warunki_czy_null_laczone(ilosc_elem)" + str(len(warunki_czy_null_laczone)))
    
    '''

