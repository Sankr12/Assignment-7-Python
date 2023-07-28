'''
Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles triangle or not 
    b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
    c. Check whether a given set of three numbers are length of an equilateral or not
    d. Exit.
'''

print()
print("Choose which type of triangle you want to check: ")
print("1. Isosceles")
print("2. Right Angled")
print("3. Equilateral")
print()
choice = int(input("Enter Your Choice: "))
print()

match choice:
    case 1:
        a = float(input("Enter the first side of triangle: "))
        b = float(input("Enter the second side of triangle: "))
        c = float(input("Enter the third side of triangle: "))
        print()
        if((a==b and a!=c) or (a==c and a!=b)):
            print("It's an isosceles tirangle")
        elif((b==a and b!=c) or (b==c and b!=a)):
            print("It's an isosceles triangle")
        elif((c==a and c!=b) or (c==b and c!=a)):
            print("It's an isosceles triangle")
        else:
            print("It's not an isosceles triangle")
    case 2:
        a = float(input("Enter the first side of triangle: "))
        b = float(input("Enter the second side of triangle: "))
        c = float(input("Enter the third side of triangle: "))
        print()
        if(a*a==b*b+c*c):
            print("It's a right angled triangle")
        elif(b*b==a*a+c*c):
            print("It's a right angled triangle")
        elif(c*c==a*a+b*b):
            print("It's a right angled triangle")
        else:
            print("It's not a right angled triangle")
    case 3:
        a = float(input("Enter the first side of triangle: "))
        b = float(input("Enter the second side of triangle: "))
        c = float(input("Enter the third side of triangle: "))
        print()
        if(a==b and b==c):
            print("It's an equilateral triangle")
        elif(a==c and b==a):
            print("It's an equialteral triangle")
        else:
            print("It's not an equilateral triangle")
    case _:
        exit()
print()