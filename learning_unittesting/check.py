import concurrent.futures


def _return_type(b, counter):
    if counter == 0:
        return 'dict'
    elif counter == 1:
        return 'list'
    elif counter == 2:
        return 'tuple'

    else:
        raise ValueError('Invalid Input')


def _create_dict(arr, b):
    d = {}
    counter = 0
    final_list = []

    for i in arr:
        if counter==3:
            counter=0
        if i not in d.keys():
            d_t = _return_type(b[counter], counter)
            d[i] = [d_t,[i]]

        else:
            d[i][-1].append(i)
        counter += 1

    print(d)
    return d


if __name__ == '__main__':
    input_list = [1,2,3,4,5,5,1,1,3,6]
    b = [{}, [], ()]

    final_dict=_create_dict(input_list, b)

    trnspose_list=[]
    for _, value in final_dict.items():
        if value[0]=='dict':
            trnspose_list.append(dict(value[-1]))
        elif value[0]=='list':
            trnspose_list.append(value[-1])
        elif value[0]=='tuple':
            trnspose_list.append(tuple(value[-1]))

    print(trnspose_list)

