# Write a python script to display the number of days in a given month number

month = int(input("Enter the month number: "))

match month:
    case x if x == 2:
        print("28 or 29 Days")
    case x if 1 <= x <= 12 and (x in {1, 3, 5, 7, 8, 10, 12}):
        print("31 Days")
    case x if 1 <= x <= 12 and (x in {4, 6, 9, 11}):
        print("30 Days")
    case _:
        print("Invalid month")
