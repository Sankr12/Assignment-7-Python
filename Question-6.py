# Write a python script to check whether a given string is multiword string or single word string using match case statement

print()
string = input("Enter a String: ")
length = len(string)

match length:
    case 1:
        print("Single Word String")
    case _:
        print("Multiword String")

print()