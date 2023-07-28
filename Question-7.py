# Write a python program to check whether a given number is negative, positive, or zero using match case statement
print()
num = int(input("Enter a number: "))
if(num>0):
    case = 1
elif(num<0):
    case = 2
else:
    case = 3

match case:
    case 1:
        print("Positive")
    case 2:
        print("Negative")
    case 3:
        print("Zero")
print()