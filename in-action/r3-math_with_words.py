import nlpia as nlp
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import nltk

sentence = """The faster Harry got to the store, the faster Harry,the faster, would get home."""
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())

print(tokens)
#['the', 'faster', 'harry', 'got', 'to', 'the', 'store', ',', 'the', 'faster', 'harry', ',', 'the', 'faster', ',', 'would', 'get', 'home', '.']

bag_of_words = Counter(tokens)
print(bag_of_words)
#Counter({'the': 4, 'faster': 3, ',': 3, 'harry': 2, 'got': 1, 'to': 1, 'store': 1, 'would': 1, 'get': 1, 'home': 1, '.': 1})

from nlpia.data.loaders import kite_text
tokens = tokenizer.tokenize(kite_text.lower())


nltk.download('stopwords', quiet=True)
stopwords = nltk.corpus.stopwords.words('english')
tokens = [x for x in tokens if x not in stopwords]
kite_counts = Counter(tokens)

print(kite_counts)


from nlpia.data.loaders import harry_docs as docs
doc_tokens = []
for doc in docs:
     doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
print(len(doc_tokens[0]))
