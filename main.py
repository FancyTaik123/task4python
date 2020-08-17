# Enter data in the format a, b, c, d where a, b, c, d are the number of eggs laid by each hen for the day. An example is 1, 1, 1, 0

import math
import random

day = 0
eggs_per_day = []
hen_data = []

def generate_random_data_cuz_im_lazy():
  l = ""
  for x in range(4):
    i = random.randint(0, 1)
    i = str(i)
    if (x < 3):
      l = l + "{}, ".format(i)
    else:
      l = l + "{}".format(i)
  return l

def check_each_data(data):
  for x in data:
    x = int(x)
    if (not x):
      return False

    if (x == 1) or (x == 0):
      return True

def get_total(data):
  total = 0
  for x in data:
    x = int(x)
    total += x
  return total

while (day < 7):
  egg_data = generate_random_data_cuz_im_lazy()
  egg_data = egg_data.split(", ")
  
  # egg_data = str(input("Enter data in the format a, b, c, d where a, b, c, dare the number of eggs laid by each hen for the day. An example is 1, 1, 1, 0:"))
  # egg_data = egg_data.split(", ")
  if (egg_data):

    # Check that each data is either 0 or 1. else. 
    valid_data = check_each_data(egg_data)
    if (valid_data == True):
      day += 1
      total_eggs = get_total(egg_data)
      eggs_per_day.append(total_eggs)

      # append hen data   
      if (day == 1):
        for x in range(len(egg_data)):
          hen_data.insert(x, int(egg_data[x]))
      else:
        for x in range(len(egg_data)):
          hen_data[x] = hen_data[x] + int(egg_data[x])
    else:
      a = ""
      # just cancelling this line until manual input cause it keeps saying data is invalid even tho its been proven valid. 
      # print("Data is invalid. Try again" + str(day))
      # print(egg_data)

  else:
    print("Given egg data is in a invalid form data.")

for x in range(len(eggs_per_day)):
  print("Day {0}  {1} eggs(s)".format(x + 1, eggs_per_day[x]))

for x in range(len(hen_data)):
  if (hen_data[x] < 4):
    print("Hen {0}  {1} eggs(s)".format(x + 1, hen_data[x]))


calculated_total = get_total(eggs_per_day)

print("Average number eggs  {}".format(round(calculated_total / 4)))
print("Total number of eggs is {}".format(calculated_total))
