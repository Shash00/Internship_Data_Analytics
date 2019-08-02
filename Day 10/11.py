import re

data = "Learning- Python, is fun. Python_programming is, easy"

res = re.sub('\W+|_',' ',data)

print(res)