# Decorator

# def my_decorator(func):
#     def wrap_func():  # if no print statements then print normal hello as hello() otherwise it will print additional print statements
#         print('********')
#         func()
#         print('********')
#     return wrap_func


# @my_decorator  # it enhanceses our function
# def hello():
#     print('hello')


# @my_decorator  # super boosted bye() function
# def bye():
#     print('see ya')


# # # here @my_decorator is wrapping the statement like hello2 = my_decorator(hello)

# hello()
# bye()

# ***** lil complex example ---------------------------------------------------------

# def my_decorator(func):
#     def wrap_func(x, y):  # here 'hello' is pass to wrap_fun in x so when fuc(x) calls it will print str
#         print('********')
#         func(x, y)
#         print('********')
#     return wrap_func


# @my_decorator  # same as a = my_decorator(hello)
# def yo(greetings, emoji):
#     print(greetings, emoji)


# yo('hellloooooo', ':)')


# ----------------------------------------------------------------------------------------------------

# NOTE: practical applications and why we need decorators?

# from time import time


# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'it took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long():
#     for i in range(100000000):
#         i*2


# long()

# ----------------------------------------------------------------------------------------------

# Exersice

# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     # changing this will either run or not run the message_friends function.
#     'valid': True
# }


# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         if args[0]['valid']:
#             rst = fn(*args, **kwargs)
#             #print(args)
#             #print(kwargs)
#             #print(type(args))
#             return rst
#     return wrapper


# @authenticated
# def message_friends(user):
#     print('message has been sent')


# message_friends(user1)
