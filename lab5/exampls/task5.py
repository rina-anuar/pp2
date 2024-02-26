import re

txt = "The rain in Spain 2 3"
txt1 = '12 56'

x = re.findall(r"[ri]", txt) # [] жақша ішіндегі символдардың кем дегенде біреуі 
y = re.findall(r"[a-z]", txt) # [] аралық
z = re.findall(r"[a-zA-Z]", txt) # [] қос аралық a мен z және A Z арасындвғы бір символ
t = re.findall(r"[^a]", txt) # [^..] осылардан басқасы 
n = re.findall(r"[0-5][0-9]", txt1) # #Check if the string has any two-digit numbers, from 00 to 59:

print(x)
print(y)
print(z)
print(t)
print(n)


