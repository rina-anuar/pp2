import re

txt = "The rain in Spain 2 3"

x = re.findall(r"\s", txt) # \s Кез келген пробельный символ (пробел, табуляция, конец строки и т.п.)
y = re.findall(r"\S", txt) #\S Кез келген пробельный емес символ (пробел, табуляция, конец строки и т.п.)


print(x)
print(y)