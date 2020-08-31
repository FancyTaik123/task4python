for num in range(100):
    actual_num = num + 1
    actual_num **= 2
    actual_num = str(actual_num)
    if (actual_num[-1] == "4"):
        print(f"{num + 1}^2 ends with a 4.")