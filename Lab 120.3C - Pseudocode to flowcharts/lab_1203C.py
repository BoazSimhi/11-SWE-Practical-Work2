from math import sqrt, ceil
n = int(input("Input a number: "))

if n < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")
