m = float(input("Enter the length of the chocolate bar: "))
n = float(input("Enter the width of the chocolate bar: "))
k = int(input("Enter the number of squares you want: " ))

chocolate_area = 0

# first calculate the area of the chocolate
chocolate_area = (m * n)

# now use modulus, to see if you divide it you will get a remainder or not.
if (chocolate_area % k == 0):
    print(f"It is possible to split the chocolate bar into {k} squares!")
else:
    print(f"It is not possible to split the chocolate bar into {k} squares!")