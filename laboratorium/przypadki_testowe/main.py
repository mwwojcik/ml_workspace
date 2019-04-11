import sys, re,os

script_dir = os.path.dirname(__file__)


class Kategoria:
    kategoria=""
    tekst=""

    def __init__(self,aKat,aTxt):
        self.kategoria=aKat
        self.tekst=aTxt


def porzadek(kat:Kategoria):
    return kat.kategoria

plik=open(os.path.join(script_dir,"kategoryzacja_reguly_probka_uczaca.reg"),"r",encoding="utf8")

lista=[]

for linia in plik:
    operator=linia.split(' ')[0]
    slownie=linia.replace(operator+' ',"").replace("\n","")
    lista.append(Kategoria(operator,slownie))


lista.sort(key=porzadek)


for l in lista:
    print(l.kategoria+" "+l.tekst)

index=0
for l in lista:
    index+=1
    print(",KategoriaPrzypadekTestowy("+(str(index))+",\"" + l.tekst + "\"," + "\"" + l.kategoria + "\"" + ")")







