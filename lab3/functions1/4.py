def filter_prime(num):
    i = 2
    while i*i < num:
        if num%2==0:
            return False
    i += 1
    return True

