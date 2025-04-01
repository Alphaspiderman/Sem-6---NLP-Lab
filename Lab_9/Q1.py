import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)
pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN>+}"
chunk_parser = RegexpParser(grammar)
chunk_tree = chunk_parser.parse(pos_tags)

noun_phrases = [
    " ".join(word for word, pos in subtree.leaves())
    for subtree in chunk_tree.subtrees(filter=lambda t: t.label() == "NP")
]

print("Extracted Noun Phrases:", noun_phrases)
