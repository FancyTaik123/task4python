given_hour = int(input("Enter hour: "))
day_of_time = str(input("am or pm: "))
how_many = int(input("How many hours ahead: "))

# now determine
if (day_of_time == "am"):  
    
    if (given_hour + how_many > 11):
        
    else:
        print(f"{given_hour + how_many} am")

else:
    print()