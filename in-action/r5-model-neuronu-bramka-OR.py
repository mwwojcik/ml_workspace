from random import random
import numpy as np

wejscia = [[0, 0],  # False, False
           [0, 1],  # False, True
           [1, 0],  # True, False
           [1, 1]]  # True, True

spodziewane_wyjscia = [0,  # (False OR False) gives False
                       1,  # (False OR True ) gives True
                       1,  # (True  OR False) gives True
                       1]  # (True  OR True ) gives True

prog_aktywacji = 0.5

wartosc_bias=np.random.random() / 1000

wektor_wag_wejsciowych=np.random.random(2)/1000  # Small random float 0 < w < .001

for numer_iteracji in range(5):
    liczba_poprawnych=0
    for idx,wejscie in enumerate(wejscia):
        wektor_wejsciowy=np.array(wejscie)
        poziom_aktywacji=np.dot(wektor_wejsciowy,wektor_wag_wejsciowych)+(wartosc_bias*1)

        if poziom_aktywacji>=prog_aktywacji:
            wyjscie_neuronu=1
        else:
            wyjscie_neuronu=0
        if(wyjscie_neuronu==spodziewane_wyjscia[idx]):
            liczba_poprawnych+=1

        skorygowane_wagi_wejsciowe=[]

        print('wejscie=>{}'.format(wejscie))

        for index,x in enumerate(wejscie):
            print('index={},wejscie[index]={}'.format(index,x))
            skorygowane_wagi_wejsciowe.append(wektor_wag_wejsciowych[index]+(spodziewane_wyjscia[idx]-wyjscie_neuronu)*x)

        wartosc_bias=wartosc_bias+(spodziewane_wyjscia[idx]-wyjscie_neuronu)*1
        wektor_wag_wejsciowych=np.array(skorygowane_wagi_wejsciowe)
    print('{} correct answers out of 4, for iteration {}'.format(liczba_poprawnych, numer_iteracji))