import re

txt = "a"

x = re.findall("ab*", txt)#0 ден плюс шексіздік

y = re.findall("ab+", txt)# 1 ден плюс шексіздік

z = re.findall("ab?", txt) #бір немесе нол ден шексіздіккі дейін

print(x)
print(y)
print(z)