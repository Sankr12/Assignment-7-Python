# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
print()
print("For Addition: Press 1")
print("For Subtraction: Press 2")
print("For Multiplication: Press 3")
print("For Division: Press 4")
print()
choice = int(input("Enter Your Choice for Operation: "))
print()
match choice:
    case 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a+b
        print("Answer=",c)
    case 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a-b
        print("Answer =",c)
    case 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a*b
        print("Answer =",c)
    case 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a/b
        print("Answer =",c)
    case _:
        print("Invalid Input")
print()
