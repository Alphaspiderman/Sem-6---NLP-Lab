from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

txt = "He was running away from the wild dogs"

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

tokens = word_tokenize(txt)

stems = [stemmer.stem(t) for t in tokens]
lemmas = [lemmatizer.lemmatize(t) for t in tokens]

print(f"Original String: {txt}")
print(f"Tokens: {tokens}")
print(f"Stem Words: {stems}")
print(f"Lemmas: {lemmas}")
