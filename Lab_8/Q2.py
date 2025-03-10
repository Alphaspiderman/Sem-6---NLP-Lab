import re

slang_dict = {
    "brb": "be right back",
    "gtg": "got to go",
    "lol": "laugh out loud",
    "omg": "oh my god",
    "idk": "I don't know",
    "smh": "shaking my head",
    "ttyl": "talk to you later",
}

emoji_dict = {
    ":)": "smile",
    ":D": "grin",
    ":P": "playful",
    "<3": "heart",
}


def normalize_text(text):
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    text = re.sub(r"[^\w\s:;()<>/]", "", text)

    words = text.split()
    normalized_words = []

    for word in words:
        normalized_word = slang_dict.get(word.lower(), word)
        normalized_word = emoji_dict.get(normalized_word, normalized_word)
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


test_inputs = [
    "brb :)",
    "omg, thats cool! :D",
    "ttyl, smh <3",
    "   this is   a test   :P   ",
]

for test in test_inputs:
    print(f"Original: '{test}'")
    print(f"Normalized: '{normalize_text(test)}'\n")
