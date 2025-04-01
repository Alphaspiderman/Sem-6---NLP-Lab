import spacy
from spacy import displacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def analyze_text(text):
    doc = nlp(text)

    pos_tags = [(token.text, token.pos_) for token in doc]
    print("\nPOS Tags:", pos_tags)

    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
    print("\nDependency Parsing:", dependencies)

    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    print("\nExtracted Noun Phrases:", noun_phrases)

    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("\nNamed Entities:", named_entities)

    displacy.render(doc, style="dep", jupyter=True)


text = "Apple Inc. is looking at buying a UK-based startup for $1 billion."
analyze_text(text)
