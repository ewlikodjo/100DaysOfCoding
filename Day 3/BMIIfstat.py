print("This is bmi program example")

bmi = input("enter your bmi: ")

if bmi < 18.5:
    print(f"Your bmi {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Yor {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")