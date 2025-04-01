import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

def pos_tagging(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    return pos_tags


def extract_noun_phrases(pos_tags):
    # Define a simple noun phrase chunking rule
    grammar = "NP: {<DT>?<JJ>*<NN>+}"
    chunk_parser = RegexpParser(grammar)
    chunk_tree = chunk_parser.parse(pos_tags)

    noun_phrases = []
    for subtree in chunk_tree.subtrees(filter=lambda t: t.label() == "NP"):
        noun_phrases.append(" ".join(word for word, pos in subtree.leaves()))

    return noun_phrases


text = "The quick brown fox jumps over the lazy dog."

pos_tags = pos_tagging(text)
print("POS Tags:", pos_tags)

noun_phrases = extract_noun_phrases(pos_tags)
print("Extracted Noun Phrases:", noun_phrases)