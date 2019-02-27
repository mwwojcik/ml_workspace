#kategoriaA.txt
#kategoriaB.txt
#kategoriaC.txt
#KATEGORIAD.txt

import sys, re,os

script_dir = os.path.dirname(__file__)



if len(sys.argv) !=2:
    raise ValueError("Wymagane podanie nazwy AB_XXXX ")
else:
    szukanywzorzec=sys.argv[1];

print ("Analiza dla =>" + szukanywzorzec)
katA_str=open(os.path.join(script_dir, "wejscie/kategoriaA.txt")).read()
katA=katA_str.split(",")

katB_str=open(os.path.join(script_dir,"wejscie/kategoriaB.txt")).read()
katB = katB_str.split(",")

katC_str=open(os.path.join(script_dir,"wejscie/kategoriaC.txt")).read()
katC = katC_str.split(",")

katD_str= open(os.path.join(script_dir,"wejscie/KATEGORIAD.txt")).read()
katD =katD_str.split(",")




print("\n**** WYNIK ****")
if(szukanywzorzec in katA):
    print(szukanywzorzec + "=>" + "KATA")
if (szukanywzorzec in katB):
    print(szukanywzorzec + "=>" + "KAT_B")
elif (szukanywzorzec in katC):
    print(szukanywzorzec + "=>" + "KAT_C")
elif (szukanywzorzec in katD):
    print(szukanywzorzec + "=>" + "KAD_D")
else :
    print ("Nazwa nieodnaleziona")
print("***************")
