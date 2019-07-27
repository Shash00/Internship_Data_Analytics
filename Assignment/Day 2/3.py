time_table = {"MON" : [3, 2, 2],"TUE" : [3, 2, 2],"WED" : [3, 2, 2],"THU" : [3, 2, 1],"FRI" : [3, 2, 1],"SAT" : [3, 1, 0],"SUN" : [0, 0, 0]}

day = input("Enter day : ").upper()
keys = time_table.keys()
if day in keys:
    print(time_table[day])
else:
    print("Invalid Day")