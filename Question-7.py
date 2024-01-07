# Write a python program to check whether a given number is negative, positive, or zero using match case statement

print()
num = int(input("Enter a number: "))

match num:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")
print()
