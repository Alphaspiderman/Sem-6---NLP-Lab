import re

txt = "I'm excited for the upcoming concert! It will be #fun"

filtered = re.sub(r"[^a-zA-Z0-9\s]", "", txt)

print(f"Filtered: {filtered}")
