number_one = float(input("Enter number 1: "))
number_two = float(input("Enter number 2: "))

# now determine
if (number_one == number_two):
    print("Close")
elif (abs(number_one - number_two) < 0.001):
    print("Close")
elif (abs(number_two - number_one) < 0.001):
    print("Close")
else:
    print("Not close")