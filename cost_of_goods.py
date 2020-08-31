cost = 0

amount_of_items = int(input("Enter the amount of items that you bought: "))

if (amount_of_items > 0):

    # if less than 10 items
    if (amount_of_items < 10):
        cost = (amount_of_items * 7)
    elif (amount_of_items >= 10) and (amount_of_items <= 99):
        cost = (amount_of_items * 10)
    else:
        cost = (amount_of_items * 7)

    print("The total cost is ${}".format(cost))

else:
    print("You have inputted a number less that 1.")