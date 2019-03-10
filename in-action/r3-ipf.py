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

print(len(kite_intro_tokens))
print(len(kite_history_tokens))

#obliczamy TF słowa 'kite' dla każdego z dokumentów
intro_counts = Counter(kite_intro_tokens)
history_counts=Counter(kite_history_tokens)

intro_tf={}
history_tf={}

intro_tf['kite']=intro_counts['kite']/len(kite_intro_tokens)
history_tf['kite']=history_counts['kite']/len(kite_history_tokens)

print('Term Frequency of "kite" in intro is: {:.4f}'.format(intro_tf['kite']))
print('Term Frequency of "kite" in history is: {:.4f}'.format(history_tf['kite']))