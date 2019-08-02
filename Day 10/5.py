import re

data = "192.168.2.1"

res = re.findall(r"\d{3}.\d{3}.\d+.\d+", data)

print(res)