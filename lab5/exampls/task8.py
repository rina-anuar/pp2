import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^he", txt)

print(x)