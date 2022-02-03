print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would like to give? 10, 12, or 15?"))
people = int(input("How many people to split bill?"))
#bill_with_tip = tip / 100 * bill + bill

# bill_with_tip = bill * (1 + tip /100)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount} dollar")
#print(f"Each person should pay: ${final_amount}")

#print(bill_with_tip)