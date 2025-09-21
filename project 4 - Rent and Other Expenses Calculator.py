while True:
 try:
  rent = float(input("Enter your hostel/flat rent = "))
  break
 except:
   print("Invalid input! Please enter only numbers.")

while True:
 try:
   food = float(input("Enter the amount of total ordered food = "))
   break
 except:
   print("Invalid input! Please enter only numbers.")

while True:
 try:
  electricity_spend = float(input("Enter the total unit of electricity spend = "))
  break
 except:
    print("Invalid input! Please enter only numbers.")


while True:
 try:   
  charge_per_unit = float(input("Enter the charge per unit = "))
  break
 except:
   print("Invalid input! Please enter only numbers.")

while True:
 try:   
  other = float(input("Enter the amount of other expences = "))
  break
 except:
   print("Invalid input! Please enter only numbers.")

while True:
 try:
    persons = int(input("Enter the number of person living in hostel/flat = "))
    break
 except:
    print("Invalid input! Please enter only integer numbers.")


total_electricity_bill = (electricity_spend * charge_per_unit)
Total = (rent + food + total_electricity_bill + other) / persons

print("Each person has to pay = ", Total)