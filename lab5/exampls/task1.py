import re

txt = "The rain in Spain"

x = re.findall(".", txt) # . кез келген символ нол және \n басқа 

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
