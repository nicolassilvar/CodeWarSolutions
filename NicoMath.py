def factor_list(n):

    #Generate the factor list of a number
    factor_n = []
    i = 1

    while i < 1 + int(n/2):
        if n % i == 0:
            factor_n.append(i)
        i += 1

    #Return factor list
    return factor_n

def Is_amicable(n,m):

    return None

