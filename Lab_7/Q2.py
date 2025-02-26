import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def custom_tokenizer(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)

    text = re.sub(r"[^\w\s]", "", text)

    tokens = word_tokenize(text)
    return tokens


txt = "Check out the new blog post at https://example.com/blog-post! Thanks to @user for the amazing support #inspiration #coding."

tokens = custom_tokenizer(txt)

porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

stemmed = [porter_stemmer.stem(token) for token in tokens]
lemmatized = [wordnet_lemmatizer.lemmatize(token) for token in tokens]

print(f"Original text: {txt}")
print(f"Tokens: {tokens}")
print(f"Stems: {stemmed}")
print(f"Lemmas: {lemmatized}")
