COLLECTED_NUMBERS = []

collected_data = int(input("Enter a number: "))

while (collected_data != 0):
    COLLECTED_NUMBERS.append(collected_data)
    collected_data = int(input("Enter a number: "))

if (len(COLLECTED_NUMBERS) > 0):
    COLLECTED_NUMBERS = reversed(COLLECTED_NUMBERS)
    for x in COLLECTED_NUMBERS:
        print(x)
else:
    print("No data collected.")
