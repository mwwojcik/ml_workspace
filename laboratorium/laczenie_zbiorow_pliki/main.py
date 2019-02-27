
import sys, re,os

script_dir = os.path.dirname(__file__)

plik=open(os.path.join(script_dir,"wejscie/zbiorA.txt"),"r")

zbiorA=[];
for linia in plik:
    pola=linia.split("/")
    zbiorA.append(pola[len(pola) - 1].replace(".as", "").replace("\n", ""))

with open(os.path.join(script_dir,"wejscie/zbiorB.txt")) as f_in:
    zbiorB = [l for l in (line.strip() for line in f_in) if (("#" not in l) and (len(l) != 0))]
#wylaczone=list(filter(None, wylaczone))
zbiorB = [element.replace(".as", "") for element in zbiorB]


listawynikowa= zbiorA + zbiorB

print ("zbiorA=>" + str(len(zbiorA)) + " zbiorB=>" + str(len(zbiorB)))

listapu=",".join(listawynikowa)
open(os.path.join(script_dir,"zbior_A_zbiorB.txt"),"w").write(listapu)
