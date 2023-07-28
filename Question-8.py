''' Write a python script to check whether two given strings are identical, first string 
comes before the second in dictionary order or first string comes after the second 
string in dictionary order using match case statement '''

print()
string1  = input("Enter first string: ")
string2 = input("Enter second string: ")

if(string1<string2):
    case = 1
elif(string1>string2):
    case = 2
else:
    case = 3

match case:
    case 1:
        print("First String comes first")
    case 2:
        print("Second string comes first")
    case 3:
        print("Strings are identical")
    case _:
        print("Invalid input")
print()