numbers = []

for x in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

for x in numbers:
    if (x > 10):
        print(f"{x} is greater than 10!")
    if (x > 0):
        print(f"{x} is greater than 0!")