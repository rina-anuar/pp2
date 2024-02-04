import math
r = int(input())

def vol(rr):
    v = (4/3) * math.pi * pow(rr, 3)
    return v
print(vol(r))