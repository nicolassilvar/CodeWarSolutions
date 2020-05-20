import re

SS = "Strength"

pattern = re.compile(r'[^aeiou]+')

found = pattern.findall(SS)

print(found)
