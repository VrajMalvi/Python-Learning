# LINK: https://docs.python.org/3/library/pdb.html

# pdb - python debugger it is py library
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(5, 'hsh')

# it will print return num1+num2 and in new line
# (pdb) here we can type num1 or num2 and in terminal it will give values
# also (pdb) help command opens all the commands we can utilize
# before step type clear and then give y
# (pdb) step
# a commands prints all arguments
# continue will run untill return
# exit to exit (pdb)
# we change var value in and check if code will runcou (pdb)
