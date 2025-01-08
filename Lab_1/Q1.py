import re

txt = "This is some,very interesting sample text! I'm sure about it"
words = re.split(r"[^\w+]", txt)

print(words)