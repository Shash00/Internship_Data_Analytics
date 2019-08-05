import re

inp = "1007 Lakshman 1008 Karthik 1009-Ramesh -1010 Suresh"

res = re.findall(r"\d+",inp)

print(res)