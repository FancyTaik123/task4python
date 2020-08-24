import math
barcode_upca = str(input("Enter first 11 digits of UPCA-A: "))
barcode_flag = False
valid_barcode_amount = 0

result = 0
even_result = 0
odd_result = 0
remainder = 0
check_digit = 0

while (not barcode_flag==True):
  # first check if has 11 digits
  if (len(barcode_upca) < 11) or (len(barcode_upca) > 11):
    print("Invalid input, please re-enter")
  else:
    # now check if all are numbers
    for x in range(len(barcode_upca)):
      if (barcode_upca[x].isnumeric()):
        valid_barcode_amount += 1
    
    if (valid_barcode_amount == 11):
      barcode_flag = True
    else:
        print("Invalid input, please re-enter")

if (barcode_flag == True):
  for x in range(11):
    if ((x+1) % 2 == 0):
      even_result += int(barcode_upca[x])
    else:
      odd_result += int(barcode_upca[x])

  result = even_result * 3
  result += odd_result

  # now get the remainder 
  remainder = result / 10
  if (remainder == 0):
    check_digit = 0
  else:
    check_digit = 10 - remainder 

print("The UPCA is {}".format(barcode_upca))
print("Check digit is {}".format(math.floor(check_digit)))



# total_even = 0
# total_odd = 0
# num = 12345678910
# edited_num = str(num)
# for x in range(11):
#   if ((x+1) % 2 == 0):
#     print("This is a even number position")
#     print(str(edited_num[x]))
#     total_even += int(edited_num[x])
#   else:
#     print("This is a odd number position")
#     print(str(edited_num[x]))
#     total_odd += int(edited_num[x])
  

# print(total_even)
# print(total_odd)
