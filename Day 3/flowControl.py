print("Welcome to the rollercoaster !")
height = int(input("What is your height in cm ?"))

if height > 120:
    print("You can read the rollercoaster ")

else:
    print("Sorry, you have to grow taller befor you can ride.")

    age = int(input("enter your age?"))

    if age >= 18:
        print("you are eligible!")

    else:
        print("you are not eligible!")