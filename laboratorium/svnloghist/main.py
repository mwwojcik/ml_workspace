import subprocess
import re

#### Parametry ####
urls = ['https://svn.xxx/xxx'
    , 'https://svn.xxx.xxxx.xxx']

dataOd = '2018-01-01'
dataDo = '2018-01-30'
uzytkownik = 'mariusz.wojcik'


#### koniec parametry #####

class Raport:
    tresc = ""
    tytul=""

class RaportLog(Raport):
    tytul = "Raport wykonanych operacji"


class RaportPliki(Raport):
    tytul = "Raport zmienionych plikow"


def dodaj_naglowek(raport: Raport, aRepo):
    raport.tresc = raport.tresc + '\n***************************************************************************' \
                   + '\n*** '+raport.tytul+   '\n*** Repozytorium       : ' \
                   + aRepo + '\n*** Autor              : ' + uzytkownik \
                   + '\n*** Raport dla okresu  : '+ dataOd + ' - ' + dataDo \
                   + '\n*************************************************************************\n\n'
    return


def drukuj_do_pliku(nazwaPliku, zawartoscTxt: Raport):
    with open(nazwaPliku, "w", -1, 'cp1252') as text_file:
        text_file.write(zawartoscTxt.tresc)
    return


def podaj_pelnego_loga_svn(aRepo,raportLog:RaportLog):
    wyjscie = subprocess.check_output(
        'svn log ' + aRepo + ' -v -r {' + dataOd + '}:{' + dataDo + '} --search ' + uzytkownik + '')

    # wynik zwracany jest binarnie, trzeba zamienic na str
    # trzeba zgadnac w jakim kodowaniu
    wyjscie = wyjscie.decode('cp1252')
    raportLog.tresc=raportLog.tresc+'\n'+wyjscie;

    return wyjscie


def podaj_liste_sciezek(aLogSvn,raportPliki:RaportPliki):
    # jako sciezke traktuje linie ktora pasuje do wzorca znak_bialy [A lub M] znak_bialy reszta sciezki
    # wykluczamy operacje D (usuwanie)
    plik_re = re.compile('\s[M,A]\s.+')
    # usuwamy operacje zmiany nazwy ktore maja slowo FROM
    sciezki = [sciezka.replace(' A ', '').replace(' M ', '') for sciezka in plik_re.findall(aLogSvn) if
               'from' not in sciezka]
    # usuwam duplikaty
    sciezki = set(sciezki)
    # i z powrotem lista
    sciezki = list(sciezki)

    for sciezka in sciezki:
        raportPliki.tresc=raportPliki.tresc+'\n'+sciezka

    return sciezki


def drukuj_raport_dla_repozytorium(aRepo, raportLog: RaportLog, raportPliki: RaportPliki):
    dodaj_naglowek(raportLog, aRepo)
    dodaj_naglowek(raportPliki, aRepo)

    log=podaj_pelnego_loga_svn(aRepo,raportLog)
    podaj_liste_sciezek(log,raportPliki)

    return


def drukuj_raport_calkowity():
    raportLog = RaportLog()
    raportPliki = RaportPliki()

    for repo in urls:
        drukuj_raport_dla_repozytorium(repo, raportLog, raportPliki)

    drukuj_do_pliku("raport-log.txt", raportLog)
    drukuj_do_pliku("raport-pliki.txt", raportPliki)


drukuj_raport_calkowity()

# linie = wyjscie.splitlines()
# nowakolekcja=[funkcja konwertujaca,       iteracja       , filtr
# rewizje = [re.search('r\d*', i).group(0) for i in linie if uzytkownik in i]


# for rew in rewizje:
#    zmienionoWrewizji = subprocess.check_output('svn log ' + url + ' --verbose -r ' + rew.replace('r', '') + '').decode(
#        'cp1252')
#   raport = raport + "\n" + zmienionoWrewizji
# z raportu wybieram pliki sciezki do plikow

# drukuj_do_pliku("raport.txt", wyjscie)
print("**** Koniec ***")
