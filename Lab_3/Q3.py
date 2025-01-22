import random

word = "CARRIED"
print(f"Word: {word}")
for i in range(random.randint(1, len(word))):
    s = random.randint(1, len(word) - 1)
    print(f"Split at {s}: {(word[:s], word[s:])}")
