import numpy as np
#Budujemy one-hot vectors - wektory stanowiące numeryczną reprezentację każdego słowa

sentence=sentence = """Thomas Jefferson began building Monticello at the age of 26."""
token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))

print(token_sequence)
print(vocab)

num_tokens = len(token_sequence)
vocab_size = len(vocab)

#kazdy wiersz ma tyle kolumn ile slow jest w sentencji
onehot_vectors = np.zeros((num_tokens,vocab_size), int)

#wedrujemy przez kolejne slowa w sentencji. Odnajdujemy pozycje slowa w posortowanym wokabularzu i w kolumnie
#odpowiadajacej tej pozycji wstawiamy 1. Reszta 0
for i, word in enumerate(token_sequence):
     onehot_vectors[i, vocab.index(word)] = 1

print(onehot_vectors)

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