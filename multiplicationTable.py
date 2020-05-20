def multiplicationTable(size):
    ans = []
    for x in range(size):
        ans.append([(x+1)*i for i in range(1,size+1)])
    print(ans)
    return ans

size = 3
multiplicationTable(size)
