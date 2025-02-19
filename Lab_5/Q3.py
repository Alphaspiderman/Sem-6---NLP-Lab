import re

txt = "I have 2 apples and 3 bananas"

tokens = re.findall(r"\S+", txt)

filtered_tokens = [token for token in tokens if re.search(r"\d+", token)]

print(f"Original: {txt}")
print(f"Digits in the text: {filtered_tokens}")
