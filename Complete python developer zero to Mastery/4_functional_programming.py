# NOTE: map(), filter(), zip() and reduce()

# from functools import reduce


# mylist = [2, 3, 5, 4]

# # ******** map


# def mult(iteam):
#     return iteam*2  # we pass multi value to map so map creates list and we can get value only by converting map to list


# print(list(map(mult, mylist)))  # no need to use bracket()

# # ********** filter


# def only_odd(iteam):
#     return iteam % 2 != 0   # filter accepts bool to filter and make list


# print(list(filter(only_odd, mylist)))  # no need to use bracket()


# # ******** zip

# your_list = [10, 20, 30]
# their_list = (7, 8, 9)

# # combine two iterables like zipper if different length then minimum is considered and it return list of tuples
# print(list(zip(your_list, mylist, their_list)))


# # ********** reduce

# # we have to import reduce
# #from functools import reduce


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item  # hree it will print from 0 and first item of item then both are added and return which will be next acc for first instace 0 is given while we called


# print(reduce(accumulator, mylist, 0))

# --------------------------------------------------------------------------------------------------

# NOTE: exersice for above methods

# from functools import reduce

# # 1 Capitalize all of the pet names and print the list


# def upper(iteam):
#     return iteam.upper()


# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# print(list(map(upper, my_pets)))


# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
# print(list(zip(my_strings, sorted(my_numbers))))


# # 3 Filter the scores that pass over 50%


# def passing(iteam):
#     return iteam >= 50


# scores = [73, 20, 65, 19, 76, 100, 88]
# print(list(filter(passing, scores)))

# # 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


# print(reduce(accumulator, (my_numbers + scores)))


# --------------------------------------------------------------------------------------------

# NOTE : lambda

# from functools import reduce

# mylist = [2, 3, 5, 4]

# print(list(map(lambda item: item * 2, mylist)))

# print(list(filter(lambda item: item % 2 != 0, mylist)))

# print(reduce(lambda acc, item: acc + item, mylist))

# -------------

# exersice


# # square
# my_list = [5, 4, 3]
# print(list(map(lambda item: item ** 2, my_list)))


# # sort  IMP /*/**/**/*/*/*/*/
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)


# ---------------------------------------------------------------------------------------------------


# NOTE : Comprehension

# # list
# my = [char for char in 'hello']
# my_list2 = [num for num in range(0, 50)]
# my_list3 = [num**2 for num in range(0, 50)]
# my_list4 = [num**2 for num in range(0, 50) if num % 2 == 0]


# print(my)
# print(my_list2)
# print(my_list3)
# print(my_list4)


# # set

# my_set = {char for char in 'hello'}
# my_set2 = {num for num in range(0, 50)}
# my_set3 = {num**2 for num in range(0, 50)}
# my_set4 = {num**2 for num in range(0, 50) if num % 2 == 0}

# print(my_set)
# print(my_set2)
# print(my_set3)
# print(my_set4)


# # dictonaries

# simple_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# my_dict = {key: value**2 for key, value in simple_dict.items()}

# my_dict1 = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

# my_dict2 = {num: num*2 for num in [1, 2, 3]}

# print(my_dict)

# print(my_dict1)

# print(my_dict2)


# -------------------------------------------------------------------------

# Exersice : - multi line code to comprehension


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


# ---- long lines
# dup = []
# for i in some_list:
#     if some_list.count(i) > 1:
#         if i not in dup:
#             dup.append(i)

# print(dup)
# ----- long code ends

#------ comprehension

# NOTE - we used set to remove duplicates

dup = list(set([iteam for iteam in some_list if some_list.count(
    iteam) > 1]))
print(dup)
