in_degrees = []
in_farenheit = []

for x in range(101): # 101 because first number is 0 so it ends at 99
    # check if can be divided by 10 to see if multiple
    if (x % 10 == 0):
        in_degrees.append(x)
        f = (x * 1.8) + 32
        in_farenheit.append(f)
        
for x in range(len(in_degrees)):
    deg = in_degrees[x]
    far = in_farenheit[x]
    print(f"{deg}°C --- {far}°F")