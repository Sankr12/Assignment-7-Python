'''
Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles triangle or not 
    b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
    c. Check whether a given set of three numbers are length of an equilateral or not
    d. Exit.
'''

print()
while True:
    print("Choose which type of triangle you want to check: ")
    print("1. Isosceles")
    print("2. Right Angled")
    print("3. Equilateral")
    print("4. Exit")
    print()

    choice = int(input("Enter Your Choice: "))
    
    if choice == 4:
        break

    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the second side of the triangle: "))
    c = float(input("Enter the third side of the triangle: "))
    print()

    match choice:
        case 1:
            if (a == b and a != c) or (a == c and a != b) or (b == a and b != c) or (b == c and b != a) or (
                    c == a and c != b) or (c == b and c != a):
                print("It's an isosceles triangle")
            else:
                print("It's not an isosceles triangle")
        case 2:
            if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
                print("It's a right-angled triangle")
            else:
                print("It's not a right-angled triangle")
        case 3:
            if a == b == c:
                print("It's an equilateral triangle")
            else:
                print("It's not an equilateral triangle")
        case _:
            print("Invalid choice")
print()
