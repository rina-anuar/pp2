import re

txt = "1023"

x = re.findall(r"[0123]", txt) # сөз басы 
y = re.findall(r"0123", txt) # сөз соңы  

print(x)
print(y)