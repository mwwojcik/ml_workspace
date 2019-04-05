import sys, re,os

script_dir = os.path.dirname(__file__)

plik=open(os.path.join(script_dir,"kategoryzacja_reguly_probka_uczaca.reg"),"r")

for linia in plik:
    operator=linia.split(' ')[0]
    slownie=linia.replace(operator+' ',"").replace("\n","")


    print(",KategoriaPrzypadekTestowy(\""+slownie+"\","+"\""+operator+"\""+")")