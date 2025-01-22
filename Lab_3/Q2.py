word = "CARRIED"
print(f"Word: {word}")
print(f"All prefixes: {[word[:i] for i in range(1, len(word))]}")
print(f"All suffixes: {[word[i:] for i in range(1, len(word))]}")
