from nltk.corpus import brown

#import nltk
#nltk.download('brown')

'''
The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University. 
This corpus contains text from 500 sources, and the sources have been categorized by genre, 
such as news, editorial, and so on.[63]
'''
print(brown.words()[:10])

from collections import Counter
puncs = set((',', '.', '--', '-', '!', '?',':', ';', '``', "''", '(', ')', '[', ']'))
word_list = (x.lower() for x in brown.words() if x not in puncs)
token_counts = Counter(word_list)
print(token_counts.most_common(20))