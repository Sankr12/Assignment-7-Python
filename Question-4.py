''' Write a program which takes user's age and display the category of person. 
Age below 10 years - Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 - 
Experienced, Age above or equal 60 - Senior citizen. '''

print()
Age = int(input("Enter Your Age: "))

match Age:
    case x if x < 10:
        print("Kid")
    case x if 10 <= x < 20:
        print("Teen")
    case x if 20 <= x < 40:
        print("Young")
    case x if 40 <= x < 60:
        print("Experienced")
    case x if x >= 60:
        print("Senior citizen")
    case _:
        print("Invalid input")

print()
