def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

if __name__ == '__main__':
    data = list(input("Enter List: ").strip().split())
    data = list(map(int, data))
    target = int(input("Enter Target: "))
    low = int(data[0])
    high = int(data[-1])
    binary_search(data, target, low, high)
