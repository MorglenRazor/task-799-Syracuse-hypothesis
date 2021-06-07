def syracuse_hypothesis(array, arr_fin):
    array_hyp = []
    # proof of the Syracuse conjecture
    for i in array:
        # if the number is even, divide it by 2
        if i % 2 == 0:
            i = i / 2
            array_hyp.append(i)
        # if the number is odd, then multiply it by 3, add 1 and divide by 2
        else:
            i = i * 3
            i = i + 1
            i = i / 2
            array_hyp.append(i)
    a = len(array_hyp)
    i = 0
    while a != 0:
        a -= 1
        try:
            if array_hyp[i] == 1.0:
                arr_fin.append(array_hyp.pop(i))
        except IndexError:
            continue
        i += 1
    # recursively check an array of numbers if the array is not empty yet
    if array_hyp:
        syracuse_hypothesis(array_hyp, arr_fin)

    return arr_fin


if __name__ == '__main__':
    # 'arr_fin' array to write to some final result
    arr_fin = []
    # input array
    arrary = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(syracuse_hypothesis(arrary, arr_fin))
