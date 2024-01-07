'''Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''

print()
num = int(input("Enter a number: "))

match num:
    case x if x % 2 == 0:
        print("Saurabh Shukla")
    case x if x < 0 and x % 2 != 0:
        print("Prateek Jain")
    case x if x > 0 and x % 2 != 0:
        print("Aditya Chaudhary")
    case _:
        print("Invalid input")

print()
