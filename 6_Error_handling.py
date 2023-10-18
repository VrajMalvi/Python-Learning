# with continue and break
# while True:
#     try:
#         age = int(input('What is your age? : '))
#         10/age
#     except ZeroDivisionError:
#         print('please enter age higher than 0')
#         break
#     except ValueError:
#         print('please enter a number')
#         continue
#     else:                       # either else will be executed or except but not both
#         print('thank you')
#         break
#     finally:
#         print('ok, i am finally done')


# ----------------------------------------------------------------------------------------------------------


# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         # here error in great detail will be printed
#         print('please enter number' + err)
# # or
#         print(f'please enter number {err}')
# # or
#         print(err)


# print(sum(1, '2'))
# print(sum(1, 0))

# ----------------------------------------------------------------------------------------------------------------

# raise exception

# while True:
#     try:
#         a = int(input('enter number: '))

#         raise TypeError('enter degits')
#     except ZeroDivisionError:
#         print('enter value grater than zero')
#         break
#     else:
#         print('thanks')
#     finally:
#         print('ok,done.')
