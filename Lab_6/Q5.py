import re

txt = "Hi, my phone number is +99 9999999999 also +88(888)888-8888 also +77(777) 777-7777 also +66666-666-6666 also +661234567890"
numbers = re.findall(r"(\+\d{1,2})?.?(\d{3}).{0,2}(\d{3}).?(\d{4})", txt)

print(numbers)