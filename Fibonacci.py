def fibo(n):
    if n <= 1:
        print("Fibo(1)-> (a,b)",n,0)
        return (n,0)
    else:
        (a,b) = fibo(n-1)
        print("Fibo(n)-> (a,b)",a+b,a)
        return (a+b, a)

if __name__ == '__main__':
    n = int(input())
    a, b = fibo(n)
    print(a)


