from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

#Budujemy leksykon dla korpusu skladajacego sie z trzech dokumentow


docs = ["The faster Harry got to the store, the faster and faster Harry would get home."]
docs.append("Harry is hairy and faster than Jill.")
docs.append("Jill is not as hairy as Harry.")

doc_tokens = []
for doc in docs:
     doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
print(doc_tokens)
'''
[   [',', '.', 'and', 'faster', 'faster', 'faster', 'get', 'got', 'harry', 'harry', 'home', 'store', 'the', 'the', 'the', 'to', 'would']
    , ['.', 'and', 'faster', 'hairy', 'harry', 'is', 'jill', 'than']
    , ['.', 'as', 'as', 'hairy', 'harry', 'is', 'jill', 'not']]

'''
#tokeny z poszczegolnych dokumentow trafiaja do jednej listy
all_doc_tokens = sum(doc_tokens, [])
print(all_doc_tokens)
'''
[',', '.', 'and', 'faster', 'faster', 'faster', 'get', 'got', 'harry', 'harry', 'home', 'store', 'the', 'the', 'the', 'to', 'would', '.', 'and', 'faster', 'hairy', 'harry', 'is', 'jill', 'than', '.', 'as', 'as', 'hairy', 'harry', 'is', 'jill', 'not']
'''
#wybieramy unikalne tokeny ze wszystkich dokumentow, sortujemy je
lexicon = sorted(set(all_doc_tokens))
print(lexicon)
'''
[',', '.', 'and', 'as', 'faster', 'get', 'got', 'hairy', 'harry', 'home', 'is', 'jill', 'not', 'store', 'than', 'the', 'to', 'would']
'''