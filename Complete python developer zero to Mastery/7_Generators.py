# here is why we use Generators

# def make_list(num):
#     result = [num]
#     for i in range(num):
#         result.append(i)
#     return result


# my_list = make_list(1000)
# print(my_list)

# NOTE: here above method creates list of 1000 number only after completion of making list we can access them in small num we didnt get much idea but what is num is 1000000 then it would take much longer and much memory space


# solution

# def generator_function(num):
#     for i in range(num):
#         yield i*2  # we have to use next()

# # next pauses fun and remeber last value
# # if we use next more than range value then we get 'StopIteration' error


# g = generator_function(100000)
# next(g)     # 0*2
# next(g)  # 1*2
# print(next(g))  # 2*2


# we can also use for loop to reaach desire num
# for i in range(2):
#     next(g)
# print(next(g))

# -----------------------------------------------------------------------------------------------------------


# from time import time


# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     print('1')
#     for i in range(10000000):   # took some seconds
#         i*5


# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10000000)):  # took almost double time
#         i*5


# long_time()
# long_time2()

# how we should do it
# we can avoid this much memory and time westage by using gemerators
# ----


# def gen_fun(num):
#     for i in range(num):
#         yield i


# p = 0
# for iteam in gen_fun(100):
#     pass
# print(iteam)    # we get 99


# ----


# ---------------------------------------------------------------------------------------------------------
# --


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))  # only using next() will give value
#             print(iterator)  # show address not value
#         except StopIteration:
#             break


# special_for([1, 2, 3])


# --


# class MyGen():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0, 100)

# for i in gen:
#     print(i)


# --

# fibonacci series - with list it stores and use more memory
# def fib(number):
#     fib_list = [0, 1]

#     for i in range(number-1):
#         fib_list.append(fib_list[i]+fib_list[i+1])

#     return (fib_list)


# print(fib(10))

# fibonacci series - with Generator method it doesn't stored in memory

# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a           #using yield it passes value of a to for loop(x)
#         t = a
#         a = b
#         b = t+b


# for x in fib(10):
#     print(x)
