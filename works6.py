#recursiv function

# def  factorial(n):
#     # base case
#     if n == 0:
#         return 1
#     else:
#         # expensive (your computer might crash)
#         return n * factorial(n - 1)

# # www.leetcode.com
# # import sys
# # sys.setrecursionlimit(2000)

# print(factorial(3))
# for i in range(1000):
#     print(factorial(i), f'i->{i}')

# x= [1,2,3,]

# 20 minutes, trying to rewrite this to use a recursive style
# def get_sum(list):
#     total = 0
#     for i in list:
#         total += i
#     return total

# print(get_sum(x))


# def getSum1(piece):
#     print(piece)
#     if len(piece)==0:
#         return 0
#     else:
#         return piece[0] + getSum1(piece[1:]) 

# print(getSum1(x))


# def getSum2(piece):
#     return piece[0] + getSum2(piece[1:]) if piece else 0

# print(getSum2(x))

# x= [1,2,3,]

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         first = lst.pop(0)
#         return first + sum_list(lst) + sum_list(lst) 
    
# print(sum_list(x))


# names = ['vic','peer','pasco']

# for name in names:
#     print(f"Hello {name}")

# def recursive_greet(names):
#     if not names:
#         return "finito"
#     else:
#         print(f"Hello {names.pop()}")    
#         return recursive_greet(names)

# recursive_greet(names)        



#function in function nested

# def out_function():
#     x = "inner Var local var"
#     def inner_function():
#         def inner_inner_function():
#             return "inner inner Function"
#         return "I am inner Function"

# def outer(x):
#     def inner(y):
#         print('y is here')
#         return y
#     inner("Fausto")
#     return x
# print(outer('Doe')) 


# def outer(x):
#     def add_mr_miss(y):
#         return f'Mr/Ms {y}'
#     return add_mr_miss(x)

# print(outer('Doe'))

#pass function as argument

# def da _something(string, func):
#     return func(string)

# def make_upper(name):
#     retunr name.title()

# passing a function as an argument

# def do_something(string, func):
#     return func(string)

# def add_a_greeting(name):
#     return "Good morning " + name

# def make_upper(name):
#     return name.title()

# print(do_something('peer', make_upper))
# print(do_something('peer', add_a_greeting))
# print(do_something(do_something('peer', make_upper), add_a_greeting))