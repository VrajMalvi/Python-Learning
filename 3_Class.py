# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# dup = []
# count = 0
# for i in some_list:
#     if some_list.count(i) > 1:
#         if i not in dup:
#             dup.append(i)

# print(dup)


# CLass

# # Given the below class:
# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# c1 = Cat('meo', 5)
# c2 = Cat('babu', 7)
# c3 = Cat('vjj', 9)


# # 2 Create a function that finds the oldest cat
# def old(*age):
#     return max(age)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# oldest = old(c1.age, c2.age, c3.age)
# print(f'The oldest cat is {oldest} years old.')
# ----------------------------------------------------------------------------------

# @classmethod and @staticmethod

# class playerCharacter:
#     membership = True  # Class Object Attribute

#     def __init__(self, name, age):
#         self.name = name  # class Attribute
#         self.age = age  # class Attribute

#     @classmethod  # to access method outside of class without object like classname.fun()
#     # cls is necessary to include or will give error of parameter
#     def addingthings(cls, num1, num2):
#         # here cls refers to class and in return we use clas to return class object
#         return cls('jj', num1 + num2)

#     @staticmethod
#     def addingthings1(num1, num2):
#         # here we can not access the cls like before that is the difference between two
#         return (num1 + num2)


# player1 = playerCharacter('vraj', 21)
# player2 = playerCharacter.addingthings(5, 10)
# player3 = playerCharacter.addingthings1(55, 10)
# print(player1.age)
# # returns address because it return class object and how like p4 statemtnt we get data
# print(player2)
# print(player2.name, player2.age)
# print(player3)

# ----------------------------------------------------------------------------------------------


# NOTE : Inheritance Exersice

# class Pets():
#     animals = []

#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 1 Add nother Cat


# class jadu(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# # 2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon('simon', 4), Sally('sally', 6), jadu('jadu', 10)]

# # 3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)
# # 4 Output all of the cats walking using the my_pets instance
# my_pets.walk()

# --------------------------------------------------------------


# NOTE: MRO - method resolution order

# MRO is rule in case of multilev and multiple inheritance

'''
         a
       //  \\
       b    c 
       \\  //
          D
'''


# class a():
#     num = 10


# class b(a):
#     pass


# class c(a):
#     num = 1


# class d(b, c):
#     pass


# print(d.mro())  # it shows order in which it will access parent class
# print(d.num)

# ------------

# class x:
#     pass


# class y:
#     pass


# class z:
#     pass


# class A(x, y):
#     pass


# class B(y, z):
#     pass


# class M(B, A, z):
#     pass


# print(M.__mro__)  # NOTE: here first go to M then B then A then x,y,z here it uses depth first search that's why multilev and multiple inheritance is complicated and many language avoid to use

# ----------------------------------------------------------------
