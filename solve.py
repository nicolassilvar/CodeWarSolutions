def solve(s):
    #define dictionary with letter value
    ChValue = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26
    }

    val = [0] * len(s)
    i = 0
    #Loop thru the string subdiving consonant groups
    for ch in s:
        if ch not in ('a','e','i','o','u'):
           print(ch)
           val[i] = val[i] + ChValue[ch]
        else:
            i += 1

    #Return the max value group
    print(val, max(val))
    return max(val)

if __name__ == '__main__':
    s = 'strength'
    solve(s)
