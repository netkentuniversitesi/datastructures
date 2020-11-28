# /usr/bin/env python3
# -*- coding: utf-8 -*-

names = ["John", "Albert", "Newton"]

recurring_name = ["Trump", "Biden", "Biden", "Biden", "Trump"]

find_recurring = recurring_name.count("Biden")

a = [i for i in range(25)]

b = list(range(15))

sorting_names_list = ["KEMAL", "MUSA", "AHMET"]
sorting_names_list.sort(reverse=True)

if __name__ == '__main__':
    # Print list a contents
    print("a list: {0}".format(a))

    # Print list b contents
    print("b list: {0}".format(b))

    # Print the element whose index we know in list b
    print("First index of b list is : {}".format(b[0]))

    # Print names list contents
    print("names list: {0}".format(names))

    # Add new item to list b
    a.append(999)

    # Print list b contents
    print("a list add a value : {0}".format(a))

    # Print how many desired values are in a list
    print("The list recurring_names  has {0} Biden value inside".format(find_recurring))

    # Print list sorting_names_list 
    print(sorting_names_list)
