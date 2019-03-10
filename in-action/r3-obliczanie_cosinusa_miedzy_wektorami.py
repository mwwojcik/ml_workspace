import math


'''
Funkcja obliczajaca cosinus kąta pomiędzy wektorami VSM dla dwóch dokumentów. Na wejściu otrzymujemy dwa uporządkowane słowniki.
Wektory pozyskujemy z wartości słowników. 

'''

def dajCos(slownikA:dict,slownikB:dict):
    #pozyskuje VSM dla obydwu dokumentow
    wA=[wartosc for wartosc in slownikA.values()]
    wB=[wartosc for wartosc in slownikB.values()]

    #korzystam z zaleznosci cos(fi)=wAxwB/norm(wA)*norm(wB)
    iloczyn_skalarny=0

    #pobierz indeks obrotu(i) i wartosc itego elementu z wA
    for i,v in enumerate(wA):
        #zsumuj iloczyn itego elementu wA i itego elementu wB
        iloczyn_skalarny+=v*wB[i]

    normaWA=math.sqrt(sum([x*x for x in wA]))
    normaWB=math.sqrt(sum([x*x for x in wA]))

    return iloczyn_skalarny/(normaWA*normaWB)




doc1={"pierścień":0,"gondoru":1}
doc2={"pierścień":1,"gondoru":0}

print(dajCos(doc1,doc2))