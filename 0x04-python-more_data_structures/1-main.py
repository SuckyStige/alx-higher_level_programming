#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

mylist = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
newlist = search_replace(mylist, 2, 89)

print(newlist)
print(mylist)
