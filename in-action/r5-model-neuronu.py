import numpy as np

#wektor losowych liczb bliskich zero
wektor_wejsciowy=np.array([1, .2, .1, .05, .2])
#wektor losowych liczb bliskich zero
wektor_wag_wejsciowych=np.array([.2, .12, .4, .6, .90])
#losowa wartosc bias
wartosc_bias=0.2
#wartosc powodujaca aktywacje
prog_aktywacji=.5

#funkcja aktywacji (x1 * w1) + (x2 * w2) + ... + (xi * wi) + ...  -> iloczyn skalarny
wartosc_funkcji_aktywacji=np.dot(wektor_wejsciowy,wektor_wag_wejsciowych)+(wartosc_bias*1)


if wartosc_funkcji_aktywacji>=prog_aktywacji:
    wyjscie_neuronu=1
else:
    wyjscie_neuronu=0

print(wyjscie_neuronu)

