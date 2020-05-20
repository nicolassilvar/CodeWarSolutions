def find(S, val):
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return print(j)
        j += 1
    return print(-1)


if __name__ == '__main__':
    S = list(input("Enter List: ").strip().split())
    print(S)
    val = input("Enter Parameter: ")
    find(S, val)
