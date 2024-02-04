from itertools import permutations
def Per(str):
    per_list = permutations(str)

    for perm in list(per_list):
         print (''.join(perm))

str = 'ABC'
Per(str)