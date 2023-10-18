# Ternary Operator

# is_friend = True

# can_message = "message allowed" if is_friend else "now allowed to message"

# print(can_message)


# Short Circuit

# is_friend = False

# is_User = True

# if is_friend and is_User:  #or inplace of and

#     print('bff')


# For loop

# for item in 'Zero to mastery':

#     print(item)


# Iterable - list, dictonary, tuple, set, string
# user = {
#     'name' : 'vraj',
#     'age' : 206,
#     'can_swim' : False
# }
# for key, values in user.items():
#     print(key, values)
# for i in user.values():
#     print(i)
# for i in user.keys():
#     print(i)


# range()
# for _ in range(0,10,2):
#     print(_)
# for _ in range(10,0,-2):
#     print(_)
# for _ in range(0,2,1):
#     print(list(range(10)))


# enumnerate
# for i,char in enumerate(list(range(100))):
#     print(i,char)

# *arggs and **kwargs
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num=1, num2=10))

# Rule for oder : params, *args, default para, **kwargs

# ##NOTE: Walrus operator
# a = 'fdfdfsfwsefsdfsdf'
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")


# ---- global keyword
# total = 0
# def count():
#     global total #no assign just to tell we using global
#     total += 1
#     return total


# ------ nonlocal keyword
# NOTE: nonlocal means outside of current scope means not global but also not local
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
