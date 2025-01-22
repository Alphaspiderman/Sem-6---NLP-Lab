word = "CARRIED"
print(f"Word: {word}")
print(f"All possible splits: {[(word[:i], word[i:]) for i in range(1, len(word))]}")
