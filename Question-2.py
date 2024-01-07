# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

print()
while True:
    print("For Addition: Press 1")
    print("For Subtraction: Press 2")
    print("For Multiplication: Press 3")
    print("For Division: Press 4")
    print("To Exit: Press 5")
    print()

    choice = int(input("Enter Your Choice for Operation: "))
    
    if choice == 5:
        break
    elif choice>5:
        print("Invalid Choice")
        break
    else:
        pass

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print()

    match choice:
        case 1:
            print("Answer =", a + b)
        case 2:
            print("Answer =", a - b)
        case 3:
            print("Answer =", a * b)
        case 4:
            if b != 0:
                print("Answer =", a / b)
            else:
                print("Cannot divide by zero")
        case _:
            print("Invalid Input")
print()
