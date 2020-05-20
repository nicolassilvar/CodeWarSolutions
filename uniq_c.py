def uniq_c(seq):

    last = seq[0]
    counter = 1
    ans = []

    if len(seq) <= 1:
        return ans.append((last,counter))

    print(seq)
    for i in range(1,len(seq)):
        print(f'Going in with {seq[i]} and last of {last}')
        if seq[i] == last and i < len(seq) - 1:
            counter += 1
        else:
            print(f'writing in ANS: {last} and {counter}')
            ans.append((last,counter))
            counter = 1

        last = seq[i]

    print(ans)

def uniq_c2(seq):

    ans = []
    counter = 1

    if not seq:
        return None
    elif len(seq) == 1:
        print('len 1')
        print(seq[0], counter)
        return ans.append((seq, counter))

    ans.append((seq[0], counter))
    ans_counter = 0
    previous = seq[0]
    print(ans)

    for i in range(1, len(seq)):
        if seq[i] == previous:
            counter += 1
            print(seq[i], counter)
            ans[ans_counter] = (seq[i], counter)
        else:
            ans_counter += 1
            counter = 1
            ans.append((seq[i], counter))
            previous = seq[i]
        previous = seq[i]

    print(ans, len(ans))

seq = ['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c']
uniq_c2(seq)
