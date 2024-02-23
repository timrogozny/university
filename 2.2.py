year = int(input("enter year"))
if year % 4 == 0 and year % 100 != 0:
    print("year", year, "is leap")
else:
    print("year", year, "is not leap")