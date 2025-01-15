import re

txt = "?Hello World!!"
replacement_char = "*"
output = re.sub(r"[^a-zA-Z0-9]", replacement_char, txt)
print(f"Updated String - {output}")
