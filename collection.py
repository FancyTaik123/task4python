NUMBER_COLLECTION = []

collection_data = int(input("Enter a number to be collected: "))

while (collection_data != 0):
    NUMBER_COLLECTION.append(collection_data)
    collection_data = int(input("Enter a number to be collected: "))

if (len(NUMBER_COLLECTION) > 0):
    
    # now calculate average
    total = 0
    for x in NUMBER_COLLECTION:
        total += x
    print(f"{total / len(NUMBER_COLLECTION)} is the average number.")

else:
    print("There was no number collected.")