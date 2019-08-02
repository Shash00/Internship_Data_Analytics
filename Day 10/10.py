import re

emails = "krishna.t@wipro.com lakshman.a@spaneos.com lakshman.a@heraizen.edu"

res = re.findall(r"@([A-z]+).", emails)

print(res)

