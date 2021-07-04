def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            return False
        return True
    return False

year = int(input("Enter a year: "))
if isLeapYear(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is NOT a leap year.")
