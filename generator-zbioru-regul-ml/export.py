import pandas as pd

def zapisz_do_pliku(reguly:pd.Series):
    with open('probka-uczaca-wyrazenia-ne.txt', 'w',encoding='utf8') as the_file:
        for i in reguly:
            the_file.write(i+'\n')