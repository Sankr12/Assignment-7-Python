''' Write a program which takes user's age and display the category of person. 
Age below 10 years - Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 - 
Experienced, Age above or equal 60 - Senior citizen. '''
print()
Age = int(input("Enter Your Age: "))
if(Age<10):
    case = 1
elif(Age<20):
    case = 2
elif(Age<40):
    case = 3
elif(Age<60):
    case = 4
else:
    case = 5
print()
match case:
    case 1:
        print("Kid")
    case 2:
        print("Teen")
    case 3:
        print("Young")
    case 4:
        print("Experienced")
    case 5:
        print("Senior citizen")
print()