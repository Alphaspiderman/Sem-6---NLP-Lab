import re

txt = "Happy Birthday😊😀"

emojis = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

filtered = re.sub(emojis, "", txt)

print(f"Filtered: {filtered}")
