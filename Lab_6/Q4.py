import re

txt = "It was 01/01/2025 the day after 31-12-2024 aka 12/31/2024"
dates = re.findall(r"(\d{2})[/-](\d{2})[/-](\d{4})", txt)

print(dates)
