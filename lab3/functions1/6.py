s = input().split()

def my_func(st):
    s_reversed = ' '.join(list(reversed(st)))
    return s_reversed

print(my_func(s))


def my_func2(st2):
    s_reversed2 = ' '.join(reversed(st2))
    return s_reversed2

print(my_func2(s))