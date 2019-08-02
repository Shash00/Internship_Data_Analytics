import re

data = "shash is in 567800 works at Bangalore and abc in 437590 at Mangalore"

lst = re.findall(r"at\s+([A-z]+)",data)

print(lst)