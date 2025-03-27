# Lab 120.3A - Pseudocode to Python\

def process_number(x):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

count = 0
while True:
    num = int(input("Input a number: "))
    if num >= 0:
        process_number(num)
        count += 1
    else:
        print("Negative number entered. Ending input.")

    if num < 0:
        break

print("Numbers processed: " + str(count))


