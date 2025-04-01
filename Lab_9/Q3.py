import spacy

# Load multilingual models
models = {
    "en": "en_core_web_sm",
    "de": "de_core_news_sm",
}

def process_multilingual_text(text, lang="en"):
    if lang not in models:
        print(f"Language '{lang}' not supported. Defaulting to English.")
        lang = "en"
    
    nlp = spacy.load(models[lang])
    doc = nlp(text)

    pos_tags = [(token.text, token.pos_) for token in doc]
    print("\nPOS Tags:", pos_tags)

    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    print("\nExtracted Noun Phrases:", noun_phrases)

    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("\nNamed Entities:", named_entities)

text = "Hallo, wie geht es Ihnen? Ich hoffe, es geht Ihnen gut."
process_multilingual_text(text, lang="de")
