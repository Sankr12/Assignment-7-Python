''' Write a python script to check whether two given strings are identical, first string 
comes before the second in dictionary order or first string comes after the second 
string in dictionary order using match case statement '''

print()
print()
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Convert strings to lowercase for case-insensitive comparison
string1_lower = string1.lower()
string2_lower = string2.lower()

match (string1_lower < string2_lower, string1_lower > string2_lower):
    case (True, _):
        print("First string comes first")
    case (_, True):
        print("Second string comes first")
    case _:
        print("Strings are identical")
print()
