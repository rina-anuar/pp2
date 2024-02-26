import re

txt = "The rain in Spain 2 3"

x = re.findall(r"[ri]", txt) # [] жақша ішіндегі символдардың кем дегенде біреуі 
y = re.findall(r"[a-z]", txt) # [] аралық
z = re.findall(r"[a-zA-Z]", txt) # [] қос аралық a мен z және A Z арасындвғы бір символ
t = re.findall(r"[^a]", txt) # [^..] осылардан басқасы 

print(x)
print(y)
print(z)
print(t)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
