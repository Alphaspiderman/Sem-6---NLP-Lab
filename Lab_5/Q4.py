import re

txt = "Contact me at abc.mahe@manipal.edu before 02/28/2025"
tokens = txt.split()
curr = ""
patterns = [
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
]

desired_pattern = "|".join(patterns)
desired_tokens = re.findall(desired_pattern, txt)
res = []

for t in tokens:
    if re.search(desired_pattern, t):
        res.append(curr.strip())
        curr = ""
        res.append(t)
    else:
        curr += " " + t

print(f"Original text: {txt}")
print(f"Filtered text: {res}")
