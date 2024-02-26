import re

txt = "The rain in Spain 2 3"

x = re.findall(r"\w", txt) # \w Кез келген әріп және сандар және _
y = re.findall(r"\W", txt) # Любая не-буква, не-цифра и не подчёркивание
print(x)
print(y)
