## Inputs we need from the user :
# Total rent
# Total food ordered for snacks
# Electricity units spend
# Charge per unit
# Persons living in room / flat


## Output
# Total amount you've to pay is

persons= int(input("Enter the number of persons living in room/flat = "))
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))


total_bill = electricity_spend*charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ",output)