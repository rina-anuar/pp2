import re

txt = "hello world"

matches = re.findall("o", txt)#Он возвращает список всех совпадений.


print(matches)  # Output: ['o', 'o']
