
import sys, re,os

script_dir = os.path.dirname(__file__)
zbiorA=open(os.path.join(script_dir,"wejscie/zbiorA.txt"),"r").read().split("\n")

nazwy=[sciezka.split("/")[-1].replace(".as","").replace(".java","")
       for sciezka in zbiorA if ((len(sciezka)!=0)and("#" not in sciezka))]


print(nazwy)



# for sciezka in zbiorA:
#     if ((len(sciezka) != 0) and ("#" not in sciezka)):
#         nazwy.append(sciezka)
#print(zbiorA)