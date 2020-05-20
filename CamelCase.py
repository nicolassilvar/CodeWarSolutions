'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
'''

def camel_case(string):
    #Split the string into words
    StringList = string.split()
    #Loop thru each capitalizing it
    for i in range(len(StringList)):
        StringList[i] = StringList[i].capitalize()
    print(''.join(StringList))

StringTest = "Nicolas silva rueda"
StringTest2 = "camel camel camel"

camel_case(StringTest)
camel_case(StringTest2)

'''
Lessong learned from other solutions out there
string.title().replace(" ","")

I was surprised how easy it was to replace the whitespaces

'''



    
