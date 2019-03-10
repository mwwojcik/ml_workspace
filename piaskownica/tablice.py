# https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.html#Two-dimensional-Arrays
import numpy as np

# Egzamin1   #Egzamin2
# student 1      93          95
# student 2      84          100
# student 3      99          87

# inicjalnie wrzucam do jednej tablicy jednowymiarowej
oceny = np.array([93, 95, 84, 100, 99, 87])

# zmieniam tablice jednowymiarowa na dwuwymiarowa
oceny = oceny.reshape(3, 2);

#        -- axis-1 ->
#               -2  -1
#                0   1
#   |          +---+---+
#   |    -3, 0 |93 | 95|
#   |          +---+---+
# axis-0 -2, 1 |84 |100|
#   |          +---+---+
#   |    -1, 2 |99 | 87|
#   V          +---+---+

# wyswietlam wymiary tablicy => (3,2) (3wiersze,2kolumny)
print(oceny.shape)

# podzbior oceny wszystkich studentow z egzaminu 2 [wszystkie rekordy;kolumna2]
oceny_studentow_egzamin2 = oceny[0:3, 1]  # Exam 2 scores for all students
# notacja uproszczona - inny zapis dla "Wszystkie"
# brak argumentow pomiedzy operatorem : spowoduje ze zotanie ustawiony min_index:max_index
oceny_studentow_egzamin2 = oceny[:, 1]  # Exam 2 scores for all students

wyniki_ostatniego_dla_wszystkich = oceny[:, -1]  # Latest exam scores (Exam 2), for all students

# automatyczne dopelnianie indeksu
# dla tabel N wymiarowych mozna podac inteks jednego wymiaru, wtedy reszta zostanie dopelniona pustym :

wyniki_wszystkich_dla_pierwszego_studenta = oceny[0]
# print(wyniki_wszystkich_dla_pierwszego_studenta)

#*******************
#*******************
#***** indeksowanie proste i zlozone
#*******************
#*******************
# demonstrating basic indexing and advanced indexing
x = np.array([[-5, 2, 0, -7],
              [-1, 9, 3, 8],
              [-3, -3, 4, 6]])
#(3,4), trzy wiersze 4 kolumny
print(x.shape)

# Access the column-1 of row-0 and row-2.
pierwsza_kolumna_wiersz0i2=x[::2,1]

# Access the subarray of `x`
# contained within the first two rows
# and the first three columns
pierwsze_dwa_wiersze_pierwsze_trzy_kolumny=x[:2, :3]

# Assign row-0, column-0 the value -40
# and row-0, column-2 the value -50
x[0, ::2] = (-40, -50)

print(x)