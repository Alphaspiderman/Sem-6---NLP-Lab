import re
slang_dict = {
    "brb": "be right back",
    "gtg": "got to go",
    "lol": "laugh out loud",
    "omg": "oh my god",
    "idk": "I don't know",
    "bff": "best friends forever",
    "tbh": "to be honest",
    "smh": "shaking my head",
    "fyi": "for your information",
    "ttyl": "talk to you later",
}


def normalize_text(text):
    text = text.lower()

    text = re.sub(r"[!?.]+", ".", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()  
    
    words = text.split()
    normalized_words = []

    for word in words:
        normalized_word = slang_dict.get(word, word)
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


# Provided test cases
test_inputs = [
    "BRB",
    "omg, thats COOL!",
    "ttyl, smh",
    "   tHIs is   a tEsT    mEsSAGe",
]

# Testing the function
for test in test_inputs:
    print(f"Original: '{test}'")
    print(f"Normalized: '{normalize_text(test)}'\n")
