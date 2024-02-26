import re

txt = "abbb"

x = re.findall(r"a{1}b", txt)#Ровно n повторений

y = re.findall(r"a{1,3}b", txt)# От m до n повторений включительно

z = re.findall(r"a{1,}b", txt) #Не менее m повторений

t = re.findall(r"a{,2}b", txt) #Не более n повторений

print(x)
print(y)
print(z)
print(t)