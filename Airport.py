import itertools as IT

def flap_display(lines, rotors, ALPHABET):
    values = list(ALPHABET)
    result = []
    comb = []

    comb = [(list(names),moves) for names,moves in IT.zip_longest(lines,rotors)]
    #Adjust size of flap to the number of movements (rotors) given
    for x in range(len(comb)):
        if len(comb[x][1])>len(comb[x][0]):
                comb[x][0].append("A"*(len(comb[x][1])-len(comb[x][0])))
        for y in range(len(comb[x][0])):


   return True

if __name__  == '__main__':
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    lines = ['CAT']
    rotors = [[1,13,27,27]]
    flap_display(lines,rotors,ALPHABET)
