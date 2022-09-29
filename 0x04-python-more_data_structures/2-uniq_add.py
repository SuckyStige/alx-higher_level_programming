#!/usr/bin/python3
def uniq_add(my_list = []):
    res_list =[]
    res = 0

    for i in my_list:
        if i not in res_list:
            res_list.append(i)
    for uniq in res_list:
        res += uniq
    return res
