import pandas as pd

def zapisz_do_pliku(reguly:pd.Series):
    with open('encje_reguly_probka_uczaca_fragment.reg', 'w',encoding='utf8') as the_file:
        for i in reguly:
            the_file.write(i+'\n')