'''
Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''

print()
print("What's your favourite colour ?")
colour = input("Ans. ")

if("yellow" in colour):
    case = 1
elif("blue" in colour):
    case = 2
elif("orange" in colour):
    case = 3
elif("white" in colour):
    case = 4
elif("black" in colour):
    case = 5
elif("red" in colour):
    case = 6
else:
    case = 7
        
match case:
    case 1:
        print("Mondat")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

print()