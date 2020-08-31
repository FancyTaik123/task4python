credit_amount = int(input("Enter the amount of credits: "))

# now determine
if (credit_amount <= 23):
    print("This student is a freshman.")
elif (credit_amount >= 24) and (credit_amount <= 53):
    print("This student is a sophomore.")
elif (credit_amount >= 54) and (credit_amount <= 83):
    print("This student is a junior.")
else:
    print("This student is a senior.")