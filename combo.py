def combo(ite1, ite2):
    tuple_list = []
    count = 0
    for items in ite1:
        tuple_list.append((ite1[count], ite2[count]))
        count += 1
    return tuple_list

print(combo(list('abcde'), list('hijkl')))
