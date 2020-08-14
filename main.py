import math

egg_list = []
total_eggs = 0
day = 0

def calculate_eggs(i):
  total = 0
  for x in i:
    total += int(x)
  return total

def validate_egg_data(i):
  total = 0
  for x in i:
    x = int(x)
    total += x
    if (x < 0):
      return False, total
    elif (x > 1):
      return False, total  
  return True, total

while (day < 7):
  number_of_eggs = str(input("Enter the number of eggs hatched by the four hens in the form of a, b, c, d for day {}: ".format(day + 1)))
 
  eggs_data = number_of_eggs.split(", ")
  egg_length = len(eggs_data)

  # if it has 4 inputs, meaning its correct
  if (egg_length == 4):

    # check that no data has more than 1 or is lesser than 0
    is_valid, total = validate_egg_data(eggs_data)
    if (is_valid == True):
      day += 1
      egg_list.append(total)
    else:
      print("Your data is invalid. Each data cannot be more than 1 or lesser than 0")
  # if input is not valid 
  else:
    print("Data inputted is not a valid form. Please input again.")


for x in range(len(egg_list)):
  total_eggs += egg_list[x]
  print("Day {0} | {1} egg(s)".format(x + 1, egg_list[x]))

print("Average number of eggs is {}".format(math.floor(total_eggs / 7)))
print("Total number of eggs is {}".format(total_eggs))
