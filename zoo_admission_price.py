COLLECTED_AGE = []

age = str(input("Enter a age: "))
total_cost = 0

while (age != ""):
    COLLECTED_AGE.append(age)
    age = str(input("Enter a age: "))

if (len(COLLECTED_AGE) > 0):

    for user_age in COLLECTED_AGE:
        user_age = int(user_age)
        if (user_age > 2):
            if (user_age >= 3) and (user_age <= 12):
                total_cost += 14.00
            elif (user_age >= 65):
                total_cost += 18.00
            else:
                total_cost += 23.00

    print(f"The total admission to the zool will be ${total_cost}")


else:
    print("No collected data.")