#!/usr/bin/python3
def search_replace(mylist, search, replace):
    new_1 = []

    for y in mylist:
        if y == search:
            new_1.append(replace)
        else:
            new_1.append(y)
            return 
