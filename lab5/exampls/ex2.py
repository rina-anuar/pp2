import re

txt = "hello world"

match = re.search("o", txt)

print(match)

print(match.span())#тюпл индексы начала и конца совпадения

print(match.start())#индекс начала совпадения
print(match.end())#индекс конца совпадения

print(match.group())#первого совпадения указанного шаблона в строке

if match:
    print("Исходная строка совпадения:", match.string)# получить исходную строку, с которой было выполнено совпадение
else:
    print("Совпадение не найдено")

