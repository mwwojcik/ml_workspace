from nlpia.data.loaders import kite_text, kite_history
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter

tokenizer=TreebankWordTokenizer()
#tworzymy korpus składający się z dwóch tekstów poświęconych latawcom
kite_intro=kite_text.lower()
kite_history=kite_history.lower()

#obydwa dokumenty w korpusie dzielimy na tokeny
kite_intro_tokens=tokenizer.tokenize(kite_intro)
kite_history_tokens=tokenizer.tokenize(kite_history)

#zliczamy poszczególne słowa
intro_counts = Counter(kite_intro_tokens)
history_counts=Counter(kite_history_tokens)

#długości wektorów
intro_tokens_total=len(kite_intro_tokens)
history_tokens_total=len(kite_history_tokens)

intro_tf={}
history_tf={}

#obliczamy TF słowa 'kite' dla każdego z dokumentów
intro_tf['kite']=intro_counts['kite']/intro_tokens_total
history_tf['kite']=history_counts['kite']/history_tokens_total

#obliczamy TF słowa 'and' dla każdego z dokumentów
intro_tf['and'] = intro_counts['and'] / intro_tokens_total
history_tf['and'] = history_counts['and'] / history_tokens_total

#obliczamy TF słowa 'china' dla każdego z dokumentów
intro_tf['china'] = intro_counts['china'] / intro_tokens_total
history_tf['china'] = history_counts['china'] / history_tokens_total


print('TF("kite") in intro =>{:.4f}'.format(intro_tf['kite']))
print('TF("kite") in history =>{:.4f}'.format(history_tf['kite']))
print('TF("and") in intro =>{}'.format(intro_tf['and']))
print('TF("and") in history => {}'.format(history_tf['and']))

'''
TF("kite") in intro =>0.0441
TF("kite") in history =>0.0202
TF("and") in intro =>0.027548209366391185
TF("and") in history => 0.030303030303030304

Problem. Słowo 'kite' wyszło równie często używane jak słowo 'and'.
'''

'''
********
********
Badamy IDF
********
********
'''
num_docs_containing_and = 0
#doc to cały słownik
for doc in [kite_intro_tokens, kite_history_tokens]:
    if 'and' in doc:
        num_docs_containing_and += 1

num_docs_containing_kite = 0
#doc to cały słownik
for doc in [kite_intro_tokens, kite_history_tokens]:
    if 'kite' in doc:
        num_docs_containing_kite += 1

num_docs_containing_china = 0
for doc in [kite_intro_tokens, kite_history_tokens]:
    if 'china' in doc:
        num_docs_containing_china += 1

num_docs = 2
intro_idf = {}
history_idf = {}
intro_idf['and'] = num_docs / num_docs_containing_and
history_idf['and'] = num_docs / num_docs_containing_and
intro_idf['kite'] = num_docs / num_docs_containing_kite
history_idf['kite'] = num_docs / num_docs_containing_kite
intro_idf['china'] = num_docs / num_docs_containing_china
history_idf['china'] = num_docs / num_docs_containing_china


intro_tfidf = {}

intro_tfidf['and'] = intro_tf['and'] * intro_idf['and']
intro_tfidf['kite'] = intro_tf['kite'] * intro_idf['kite']
intro_tfidf['china'] = intro_tf['china'] * intro_idf['china']

print(intro_tfidf)

history_tfidf = {}

history_tfidf['and'] = history_tf['and'] * history_idf['and']
history_tfidf['kite'] = history_tf['kite'] * history_idf['kite']
history_tfidf['china'] = history_tf['china'] * history_idf['china']

print(history_tfidf)

'''
{'and': 0.027548209366391185, 'kite': 0.0440771349862259, 'china': 0.0}
{'and': 0.030303030303030304, 'kite': 0.020202020202020204, 'china': 0.020202020202020204}
'''