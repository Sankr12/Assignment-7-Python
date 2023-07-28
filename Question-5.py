'''Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''
print()
num = int(input("Enter a number: "))

if((num>0 and num%2==0) or (num<0 and num%2==0)):
    case = 1
elif(num%2!=0 and num<0):
    case = 2
else:
    case = 3

match case:
    case 1:
        print("Saurabh Shukla")
    case 2:
        print("Prateek Jain")
    case 3:
        print("Aditya Chaudhary")

print()