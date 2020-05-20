#The use of a for loop:
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

#Accomplishing the same with list comprehension
squares = [i * i for i in range(10)]
print(squares)

#List comprehension with conditional statements
sentence = 'The sky is beautiful'
vowel_count = [i for i in sentence if i in 'aeiou']
print(len(vowel_count))

#Another example
sentence = 'There is someone in your backyard'
def is_consonant(letter):
    return letter.isalpha() and letter.lower() not in 'aeiou'
consonant_count = [i for i in sentence if is_consonant(i)]
print(len(consonant_count))

'''The above example the conditional is at the end of the list, which is useful
for filtering

but when change a member value you can start with jupy  
