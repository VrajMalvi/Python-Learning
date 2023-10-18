# my_file = open('10_file-IO/test.txt')

# print(my_file.read())
# print(my_file.read())  # print nothing empty like because end of line
# my_file.seek(0)  # move courser to index 0
# print(my_file.read())  # print from index 0


# here read line reads only one line ont by one in many print statements
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())


# with read_lines method we get whole file as list divided by new lines
# print(my_file.readlines())


# my_file.close()


# ******************************************************************
# unlike abouve where we have to close file we can do it morden way where we dont have to close file also this is safe way

# with open('sad.txt', mode='w') as my_file:
#     text = my_file.write(':(')
#     # print(my_file.readlines())
#     print(text)

# most common modes are r w a(append)


# for handliing error we use tey except

# try:
#     with open('sadd.txt', mode='r+') as My_file:
#         print(My_file.read())
# except FileNotFoundError as err:
#     print('file does not exist')
#     raise err
# except IOError as err:
#     print('IO error')
#     raise err


# -----------------------------------------------------------------------

# building a translator
# we search for offline translator python package pypi
from translate import Translator


translator = Translator(to_lang="ja")

try:
    with open('trans.txt', mode='r+') as tt:
        text = tt.read()
        translation = translator.translate(text)
        # while writing some times it give unicode error then add encoding = 'utf-8' argument in open
        with open('text_ja.txt', mode='w', encoding='utf-8') as tt2:
            tt2.write(translation)
except FileNotFoundError as e:
    print("file doesn't exist.")
