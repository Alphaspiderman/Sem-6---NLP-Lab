txt = "idk man, how r u doin"

slang = {"r": "are", "u": "you", "idk": "I do not know", "doin": "doing"}

print(f"Original: {txt}")
print(f"Cleaned: {' '.join([slang.get(t, t) for t in txt.split()])}")
