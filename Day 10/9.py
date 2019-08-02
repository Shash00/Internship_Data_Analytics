import re

data = "Lakshman and Amalraj are good friends, Arjun and Aruna also are also friends with Anu"

res = re.findall(r"\bA[a-z]{4,}",data,flags = re.IGNORECASE)

print(res)