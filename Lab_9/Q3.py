import spacy

# Load multilingual models
models = {
    "en": "en_core_web_sm",
    "de": "de_core_news_sm",
}

text = "Hallo, wie geht es Ihnen? Ich hoffe, es geht Ihnen gut."
lang = "de"

nlp = spacy.load(models[lang])
doc = nlp(text)

pos_tags = [(token.text, token.pos_) for token in doc]
print("\nPOS Tags:", pos_tags)

noun_phrases = [chunk.text for chunk in doc.noun_chunks]
print("\nExtracted Noun Phrases:", noun_phrases)

named_entities = [(ent.text, ent.label_) for ent in doc.ents]
print("\nNamed Entities:", named_entities)
