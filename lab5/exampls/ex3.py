import re

txt = "My love is Tair"

result = re.split(' ', txt)#разделения строки
result1 = re.split(' ', txt, 1)#разделения строки макс раз 1


print(result)
print(result1)
