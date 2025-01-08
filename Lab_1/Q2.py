import re

txt = "It was 01/01/2025 the day after 31/12/2024"
dates = re.findall(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/(\d\d\d\d)", txt)

print(dates)