import re

data = 'blue shape red toy green'

res = re.sub('(blue|green|red|yellow)','color',data)

print(res)