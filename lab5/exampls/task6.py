import re

txt = "The rain in Spain 2 3"

x = re.findall(r"\br", txt) # сөз басы 
y = re.findall(r"n\b", txt) # сөз соңы  
z = re.findall(r"\Ba", txt) # а дан бұрын символ болуы керек  
t = re.findall(r"n\B", txt) # а дан кейін смвол болуы керек 


print(x)
print(y)
print(z)
print(t)