import re

inp = "12,14-15,18,23-2"


res = re.sub(r"-", ",", inp)

lis = list(res.split(","))
print(lis)


