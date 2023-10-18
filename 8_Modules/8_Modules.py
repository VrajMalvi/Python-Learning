import random
import Utility
import shopping.shopping_cart
# we can also import as
from shopping.shopping_cart import shop
from Utility import mul, div


print(Utility.mul(5, 2))
print(div(12, 2))
print(shopping.shopping_cart.shop('Mac book'))
print(shop('va'))

print(__name__)  # her this file imports othermodules and being run that is reasn python consider this file to be __main__ whereas in other cases it gives name of package(folder) and module(py file)

print(random.choice([1, 2, 3, 4, 5]))
my_list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(my_list)
print(my_list)


# from collections import Counter,defaultdict

# li = [1, 2, 3, 4, 5, 6, 6, 6]
# vj = Counter(li)
# # it gives counted value sam egoes for string give dict of each char count
# print(vj[2])


# dict = {'a' : 1, 'b' : 2}
# # if try to acccess 'c' it give error
# dict = defaultDict(int,{'a' : 1, 'b' : 2})
# #we can give any default value incuding lambda: 5 or 'hello'


# #dictonaries are inorder after 3.7


# import datetime
# print(datetime.date.today())

# from array import array  # array is data science topic and we optimize it by assigning type
# ar = array('i', [1, 2, 3])
# print(ar[0])
