List comprehesion - potężny mechanizm tworzenia , filtrowania list

nowa_lista=[]
for ELEMENT in stara_lista:
    jezeli czySpelniaWarunek(ELEMNENT):
        nowa_lista.append("Element nowej listy"+ELEMENT)

ten kod może być zastąpiony bardziej zwięzłą konstrukcją
nowa_lista=["Element nowej listy"+ELEMENT for ELEMENT in stara_lista if czySpelniaWarunek(ELEMNENT)]