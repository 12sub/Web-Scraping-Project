import re

txt = "WeareallonebeingsintheeyesofGod"

x = re.findall('a\?', txt)
y = re.search('s', txt)
print(y)