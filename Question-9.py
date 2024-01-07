'''Write a python script to check whether given year is
a. Non century leap year
b. Century leap year
c. Non Century Non leap year
d. century non leap year '''

year = int(input("Enter the year: "))

match (year % 100 != 0, year % 4 == 0, year % 400 == 0):
    case (True, True, _):
        print("Non-century leap year")
    case (_, True, True):
        print("Century leap year")
    case (True, False, _):
        print("Non-century non-leap year")
    case (False, _, _):
        print("Century non-leap year")
    case _:
        print("Invalid")
