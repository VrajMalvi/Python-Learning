# NOTE: to build reg expression goto regex101.com
# when match is not foound it return NONE

import re

string = 'this search inside of this text please!'

# ---


# a = re.search('this', string)  # if not found then it returns NONE
# # it print object with showing start and end index in span we access span directly
# print(re.search('this', string))
# # span = (strt,end) we can also access strt and end saperately
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())  # it gives the string that was matched ('this')


# ----

# pattern = re.compile('this')

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

# print(a)
# print(b)
# print(c)
# print(d)


# -------------------------- pass checker
# a-z small and cap num and #@$% alsi min8 char and end with degit
password = re.compile(r"[a-zA-Z0-9#@%$]{8,}\d")
string1 = 'vrajMalvi008@8'  # all condition match we get match and span
st3 = 'ggg'  # no all condition doesnt match so it will return none
check = password.fullmatch(string1)
check1 = password.fullmatch(st3)
print(check)
print(check1)
