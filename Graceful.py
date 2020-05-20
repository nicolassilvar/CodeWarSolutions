from math import ceil


def grace(bill):

    bill = bill * 1.15

    if bill < 10:
        return ceil(bill)

    zeros = int(len(str(int(bill))))
    low = 10 ** (zeros - 1)
    high = 10 ** zeros
    div = 5 * 10 ** (zeros - 2)

    for x in [z for z in range(low, high + 1) if z % div == 0]:
        if x < bill:
            continue
        else:
            return print(x)


if __name__ == '__main__':
    bill = 86
    grace(bill)
