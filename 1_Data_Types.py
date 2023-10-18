# print(bin(5))  #convert 5 to binary
# print(int('0b101', 2))    #binary to int

#***** Data types Use type(value) to find type
# int
# float
# complex
# str
# bool
# list
# tuple
# set
# dict

# Escape Sequence
# w = 'It\'s "hello" sunny'


# formatted string
# name = 'vraj'
# age = 55
# print('hi' + name + '.you are' + str(age))  #orrr easy way is fprint
# print(f'hi {name}. You are {age} years old.')
# print('hi {0}. You are {2} {1} years old.'.format(name,'dd', age))


# num = '123456789'
# #[start : stop : stepover]
# print(num[0:5])  #also work as num[:5] -1 means backwords
# print(num[0:9:2])     #also word as num[::2]
# print(num[::-1])   #reverce of string


# bool      #0 is flase 1 is true
# name = 'vraj'
# print(name == 'vraj')


# name = input('Enter your name: ')  #input will str initially
# age = int(input('Enter your age: '))
# print(f'{name} your age is: {age}') #or {int(age)}


# code challange ask for username and pass and print both but pass should be * as same length as pass
# user = input('Enter your user name: ')
# password = input('Enter your password: ')
# password_en = '*' * len(password)
# print(f'Your user name is: {user} and \n Password is: {password_en}')


# Lists
# iteams = ['notebooks', 'sunglasses', 'toys', 'graps']
# print(iteams)
# print(iteams[0::2]) #skip 2nd iteam
# iteams[0] = 'laptop'
# print(iteams)
# print(iteams[0:3])
# new = iteams        #assign var to var point to iteams
# new[0] = 'a'
# new1 = iteams[:]   #creates copy
# new1[0] = 'b'
# print(iteams)
# print(new)
# print(new1)


# Matrix
# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(mat[1][2])


# list Method
# nm = ['a', 'b', 'c', 'e', 'd']
# new = nm.append('100')    # add value to list but does not produce result
# print(nm)   #update
# print(new)  #none
# new = nm
# print(new)
# new = nm[:]
# nm.insert(5, '500')       #same as append it also dont create copy of list
# nm.extend(['25'])         #extend inbracket it must be list
# print(nm)
# pop = nm.pop()          #pop removes last value and produce result We can also use it like .pop(index)
# nm.remove('100')  #remove based on value not index and does not produce result
# new.clear()     #delete all elements 
# print(nm)
# print(pop)
# print(new)
# print(nm.index('d',0,6))        #gives index of vlue it has format of .index(value, starting index, stopindex for search)
# print('d' in nm)
# new55 = nm.copy()       # for copy
# new_1 = sorted(nm)
# print(new_1)
# print(sorted(nm))       #it doesnot modify the list insted creates copy
# print(nm)
# nm.sort()
# print(nm)
# nm.reverse()        #switching opposite indexes if we first sort then reverse then we have reverse sorted list which is lil complicated and useful
# print(nm)
# print(nm[::-1])     #reverse of nm but does not affact original nm. original is reverse sort
# print(list(range(1, 16)))
# sentence = '!'
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'vj'])      #does not efface original list but creates copy and join them by char given in var also can be done this way
# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'vj'])
# print(new_sentence)


# List unpacking
# a,b,c, *other = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)



# Dictonary - dict
# dictonary = {
#     'a' : [1,2,3],
#     'b' : 'Hello',
#     'x' : True
# }
# print(dictonary['a'][1])
# print(dictonary)
# My_list = [
#     {
#         'a' : [1,2,3],
#         'b' : 'hfh',
#         'c' : False
#     },
#     {
#         'a' : [4,5,6],
#         'b' : 'rtdrfg',
#         'c' : True
#     }
# ]
# print(My_list[1]['a'][2])
# dicto = {
#     123 : [1,2,3],
#     True : 'Hello',
#     'gg': True
# }   #works with different keys but not with [100] as key bcz list are mutable while key must be immutable
# print(dicto[123])
# print(dicto.get('age'))  #gives none bcz there no age key
# print(dicto.get('age', 55)) #here we gave it a default value
# dicto = {
#     123 : [1,2,3],
#     True : 'Hello',
#     'age': 21
# } 
# print(dicto.get('age', 55))      #prints original value bcz its there
# user = dict(name='gondhi')
# print(user)
# dicto = {
#     123 : [1,2,3],
#     True : 'Hello',
#     'gg': True
# }
# print('gg' in dicto.keys())
# print([1,2,3] in dicto.values())
# print(dicto.items())
# user2 = dicto.copy()
# print(user2)
# print(user2.clear())  ##none
# print(user2)  #{}
# print(dicto.pop(123))  #produces results
# print(dicto)
# print(dicto.popitem())  #produce results
# dicto.update({123 : [4,5,6]})
# print(dicto)


# Tuples
# # immutable and are like list
# My_tuple = (1,2,3,4,5,5,6)
# # My_tuple[1] = 5
# # print(My_tuple)     #gives error
# print(My_tuple[3])
# print(1 in My_tuple)
# #cant not sort or reverse but faster 
# new_tuple = My_tuple[1:2]
# print(new_tuple)        #single tuple has coma in the end 
# x,y,z, *other = (1,2,3,4,5,6)
# print(other)
# print(My_tuple.count(5))        #first original method of tuple
# print(My_tuple.index(5))
# print(len(My_tuple))


# Sets - unordered collection of unique object
# my_set = {1,2,3,4,5,5,6}    #auto eliminate duplicate
# print(my_set)
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# my_list = [1,5,2,6,4,5,3]   #convert it to unique iteam 
# print(set(my_list))     #list to set conversion
# # print(my_set[0])    #error
# print(5 in my_set)
# print(len(my_set))
# new = my_set.copy()
# print(list(new))

# Set Methods
# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.difference(your_set))  #compare first to second var
# my_set.discard(5)
# print(my_set)
# my_set.difference_update(your_set)  #update set with match iteams
# print(my_set)
# print(my_set.intersection(your_set))    #or
# print(my_set & your_set)
# print(my_set.intersection_update(your_set))
# print(my_set.isdisjoint(your_set))      #true if they have nothing common
# print(my_set.issubset(your_set))
# print(my_set.union(your_set)) #or
# print(my_set | your_set)
# print(my_set.issuperset(your_set))

