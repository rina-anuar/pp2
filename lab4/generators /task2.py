def evennumbers(n):
    num = 0
    while num <= n:
        if num % 2 == 0:
            yield num
        num+=1

n = int(input("Enter the start number n: "))
evens = evennumbers(n)

for evennumber in evens:
    print(evennumber)