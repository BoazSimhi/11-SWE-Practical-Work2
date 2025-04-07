from math import sqrt, ceil
n = int(input("Input a number: "))

if n < 2:
    print("Not Prime")
else:
    print("ceiling root is", ceil(sqrt(n)))
    prime = True
    for i in range(2, ceil(sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            prime = False
            print("mustn't be prime")
            break

if prime:
    print("Prime")
else:
    print("Not Prime")
