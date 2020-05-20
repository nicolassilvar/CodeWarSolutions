def unique(input_str):
    if type(input_str) is str:
        input_list = list(input_str)
    else:
        input_list = input_str

    Output_list = []
    last_item = input_list.pop(0)
    Output_list.append(last_item)

    for x in input_list:
        if x == last_item:
            continue
        else:
            Output_list.append(x)
        last_item = x

    print(Output_list)


input_str = [1,2,3]
unique(input_str)
