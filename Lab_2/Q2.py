import re

txt = "?Hello World!!"
output = re.findall(r"[^a-zA-Z0-9]", txt)
print(f"Count of non alpha-numeric - {len(output)}")