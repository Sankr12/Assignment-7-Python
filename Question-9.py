'''Write a python script to check whether given year is
a. Non century leap year
b. Century leap year
c. Non Century Non leap year
d. century non leap year '''

print()
year = int(input("Enter the year: "))

if(year%100!=0 and year%4==0):
    case = 1
elif(year%100==0 and year%400==0):
    case = 2
elif(year%100!=0 and year%4!=0):
    case = 3
else:
    case = 4

match case:
    case 1:
        print("Non Century leap year")
    case 2:
        print("Century leap year")
    case 3:
        print("Non Century non leap year")
    case 4:
        print("Century non leap year")
    case _:
        print("Default Case")
print()