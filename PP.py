def pick_peaks(arr):
    i = 1
    d = dict()
    pos = []
    value = []
    while i < len(arr) - 1:

        #Check for peak
        if is_peak(arr,i):
            #save position and value
            print("Found a peak", i, arr[i])
            pos.append(i)
            value.append(arr[i])

        (gate, j) = is_plateau_peak(arr,i)
        print(gate)
        if gate:
            #save position and value of first occurrance
            print("Found a plateau peak", i, arr[i])
            pos.append(i)
            value.append(arr[i])
            (temp, i) = is_plateau_peak(arr,i)
            print(temp)

        #check the next character
        i += 1

    #return the pos and value
    d['pos:'] = pos
    d['peaks:'] = value
    print(d)                        #For debug
    return d

def is_peak(arr,i):
    if arr[i] > arr[i-1] and arr[i+1] < arr[i]:
        return True
    else:
        return False

def is_plateau_peak(arr,i):
    if arr[i+1] == arr[i] and arr[i] > arr[i-1]:
        while i < len(arr) - 1 and arr[i] == arr[i+1]:
                i += 1
        if i < len(arr) -1:
            if arr[i] > arr[i+1]:
                print("end of plateu and found a local max")
                return True,i
            else:
                return False,i
        else:
            return False,i
    else:
        return False,i

if __name__ == '__main__':
    #arr = list(input().strip().split())
    #arr = list(map(int, arr))
    #import random
    arr = [1, 2, -1, 15, 10, 10, -1, 4, -2, 10, 9, 8, 5, 6, 20, 0, 17]
    #forin range(10):
    #    arr.append(random.randint(0,101))

    print(arr)
    pick_peaks(arr)
