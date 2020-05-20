import re

SS = '''
324.345.4567
345-234-0909
900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909900-456-3453
800-345-0909
Nicolas Silva Rueda
'''

#character sets []
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
#
#matches = pattern.finditer(SS)
#
#for match in matches:
#    print(match)
#
with open('names.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)


