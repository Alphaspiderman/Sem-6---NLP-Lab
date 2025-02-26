import re
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk


def normalize_text(text):
    text = text.lower()

    text = re.sub(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})", "date", text)
    text = re.sub(r"[^\w\s-]", "", text)

    return text


def extract_named_entities(text):
    sentences = nltk.sent_tokenize(text)
    entities = []

    for sentence in sentences:
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        ne_tree = ne_chunk(pos_tags, binary=False)

        for subtree in ne_tree:
            if hasattr(subtree, "label"):
                label = subtree.label()
                if label in ["PERSON", "ORGANIZATION", "GPE", "DATE"]:
                    entity = " ".join(token for token, pos in subtree.leaves())
                    entities.append((entity, label))

    return entities


txt = "On 12/09/2020, John Doe from Acme Corp. held a meeting in Geneva with the United Nations."

print(f"Original Text: {txt}")

named_entities = extract_named_entities(txt)
print("Named Entities (Entity, Label):")
for entity, label in named_entities:
    print(f"{entity}/{label}")
    txt = txt.replace(entity, label)


normalized_text = normalize_text(txt)
print(f"Normalized Text: {normalized_text}")
