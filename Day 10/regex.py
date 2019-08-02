import re

data = "1001 DBMS 20   1002  JS  23  1003     SQL  15"

lst = re.split(r"\s+",data)

print(lst)