import re

txt = "?Hello World!"
# output = re.sub(r"^[^a-zA-Z0-9]+", "", re.sub(r"[^a-zA-Z0-9]$", "", txt))
output = re.sub(r"^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$", "", txt)

print(output)
