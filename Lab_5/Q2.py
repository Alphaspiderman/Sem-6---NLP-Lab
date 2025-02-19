import re

txt = "I have 20 apples and 3 bananas"

digits = re.findall(r"\d", txt)

print(f"Original: {txt}")
print(f"Number of Digits: {len(digits)}")
