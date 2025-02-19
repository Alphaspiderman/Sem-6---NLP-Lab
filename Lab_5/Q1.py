import re

txt = "I have 2 apples and 3 bananas"

tokens = re.findall(r"\S+", txt)

filtered_tokens = [token for token in tokens if not re.search(r"\d+", token)]

res = " ".join(filtered_tokens)

print(f"Original: {txt}")
print(f"Cleaned: {res}")
