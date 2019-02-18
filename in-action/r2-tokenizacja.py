import numpy as np
import pandas as pd
#Budujemy one-hot vectors - wektory stanowiące numeryczną reprezentację każdego słowa

sentence=sentence = """Thomas Jefferson began building Monticello at the age of 26."""
token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))

#print(token_sequence)
#print(vocab)

'''
['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']
['26.', 'Jefferson', 'Monticello', 'Thomas', 'age', 'at', 'began', 'building', 'of', 'the']
'''

num_tokens = len(token_sequence)
vocab_size = len(vocab)

#kazdy wiersz ma tyle kolumn ile slow jest w sentencji
onehot_vectors = np.zeros((num_tokens,vocab_size), int)

#wedrujemy przez kolejne slowa w sentencji. Odnajdujemy pozycje slowa w posortowanym wokabularzu i w kolumnie
#odpowiadajacej tej pozycji wstawiamy 1. Reszta 0
for i, word in enumerate(token_sequence):
     onehot_vectors[i, vocab.index(word)] = 1

#print(onehot_vectors)

'''
sent=>['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']
voc =>['26.', 'Jefferson', 'Monticello', 'Thomas', 'age', 'at', 'began', 'building', 'of', 'the']
[[0 0 0 1(Thomas) 0 0 0 0 0 0]
 [0 1(Jefferson) 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 1(began) 0 0 0]
 [0 0 0 0 0 0 0 1(building) 0 0]
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 0]
 [1 0 0 0 0 0 0 0 0 0]]
 '''

#dodajemy opis znaczenia kolumn
pdf=pd.DataFrame(onehot_vectors, columns=vocab)
#print(pdf)

'''
   26.  Jefferson  Monticello  Thomas  age  at  began  building  of  the
0    0          0           0       1    0   0      0         0   0    0
1    0          1           0       0    0   0      0         0   0    0
2    0          0           0       0    0   0      1         0   0    0
3    0          0           0       0    0   0      0         1   0    0
4    0          0           1       0    0   0      0         0   0    0
5    0          0           0       0    0   1      0         0   0    0
6    0          0           0       0    0   0      0         0   0    1
7    0          0           0       0    1   0      0         0   0    0
8    0          0           0       0    0   0      0         0   1    0
9    1          0           0       0    0   0      0         0   0    0

'''
#sentence dzielimy na token i zwracamy (token,1), z każdej sekwencji tworzymy serię i dodajemy ją do tabeli wektorów (serii) DataFrame, otrzymaną macierz odwracamy (T),
#kolumny stają się wierszami
df = pd.DataFrame(pd.Series(dict([(token, 1) for token in sentence.split()])), columns=['sent']).T
print(df)

'''
      Thomas  Jefferson  began  building  Monticello  at  the  age  of  26.
sent       1          1      1         1           1   1    1    1   1    1

'''

#Podobna operacja z tym że sekwencje dzielimy znakiem końca linii i do DataFrame dodajemy wektor dla każdej sekwencji
sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += "He moved into the South Pavilion in 1770.\n"
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""
corpus = {}
for i,sent in enumerate(sentences.split('\n')):
     #tworzy element slownika corpus o kluczu sent0,sent1
     #element slownika to wektor odpowiadajacy tokenom z itej sekwencji (klucz=token, wartos=1)
     corpus['sent{}'.format(i)]=dict([(tok,1) for tok in sent.split()])

#utworz dataframe na podstawie corpus, Nan zamień na 0 (fillna),asType(int) domyślnie byłoby float, transponuj T
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
#df.columns[:10] - pierwszych 10 kolumn
print(df[df.columns[:10]])
