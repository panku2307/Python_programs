year = int(input("Enter the year"))

if year % 4 == 0 and year % 100 != 0:
    print(year,"It is a leap year")
elif year % 100:
    print(year,"It is not a leap year")
elif year % 400:
    print(year,"It is a leap year")
else :
    print(year,"It is not a leap year")
