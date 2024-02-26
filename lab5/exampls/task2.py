import re

txt = "The rain in Spain 2 3"

x = re.findall(r"\d", txt) # \d кез келген сан
y = re.findall(r"\D", txt) # \D кез келген сан емес символ

print(x)
print(y)
