cricket =  [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
football = [ "PKM", "ALN","RMZ","CS", "MCS"]
badminton = [ "PKM", "ALN", "NV", "KM","RMV"]

plays_all_three = list()

for player in cricket:
    if player in football and player in badminton : 
        plays_all_three.append(player)

plays_exactly_one =  [player for player in cricket if player not in football and player not in badminton]
plays_exactly_one.extend([player for player in football if player not in badminton and player not in cricket])
plays_exactly_one.extend([player for player in badminton if player not in cricket and player not in football])

print(plays_all_three)
print(plays_exactly_one)


