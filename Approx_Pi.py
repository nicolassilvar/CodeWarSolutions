import random

#Approx Pi by running a monte carlo of N data points
def approx_pi(N):

    m = 0

    for x in range(N):

        x = -1 + 2 * random . random()
        y = -1 + 2 * random . random ()

        if (x*x + y*y) <= 1:
            m += 1

    pi = 4*m/N

    return pi

N = 1000000
print(approx_pi(N))
