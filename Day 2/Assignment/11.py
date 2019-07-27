Cricket = ["PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = ["PKM", "ALN","RMZ","CS", "MCS"]
Badminton = ["PKM", "ALN", "NV", "KM", "RMV"]

d = {}
all3 = []
only1 = []

lst = [Cricket, Football, Badminton]
for i in lst:
    for j in i:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1

for key in d:
    if d[key] >= 3:
        all3.append(key)
    if d[key] == 1:
        only1.append(key)

print(f'All 3:{all3}, Only 1:{only1} ')
