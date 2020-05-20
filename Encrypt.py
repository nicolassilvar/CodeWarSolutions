def encrypt_this(text):

    #Text is a string sentece
    textList = text.split()
    EncrypList = []

    for word in text.split():
        if len(word) < 2:
            EncrypList.append(str(ord(word)))
        elif len(word) < 3:
            Temp = list(word)
            Temp[0] = ord(Temp[0])
            EncrypList.append(''.join(str(e) for e in Temp))
        else:
            Temp = list(word)
            Temp[0] = ord(Temp[0])
            Temp[1], Temp[-1] = Temp[-1], Temp[1]
            EncrypList.append(''.join(str(e) for e in Temp))
    return(' '.join(EncrypList))

if __name__== '__main__':
    text = "A wise old owl lived in an oak"
    encrypt_this(text)
