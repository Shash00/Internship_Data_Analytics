year = int(input('Enter a year:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The given year {year} is leap year")

else:
    print(f"Given year {year} is not leap year")
    