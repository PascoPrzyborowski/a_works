#Decoration

#function in Function

# def outer():
#     def inner():
#         print("Hello, I am inner")
#     return inner

# x = outer()  
# x()
# outer()()

# def outer(name):
#     def inner():
#         print(f"Hello {name}, I am inner")
#     return inner

# outer('shaban')()

# def check_divisor(func):
#     def inner(a,b):
#         if b == 0:
#             print('no zero')
#             return
#         return func(a,b)
#     return inner

# def divide(a, b):
#     # if b == 0:
#     #     print('no divide 0')
#     #     return
#     return a / b


# divide = check_divisor(divide)
# #print(divide(4, 2))
# print(divide(4, 0))

# @check_divisor
# def divide(a,b):
#     return a / b

#print(divide(4, 2))
# print(divide(4, 0))

# use in API accessing Data by url(website)
# database

#API  Application  Programming Interface
# CLI Command Line interface
#GUI Gaphical user inface
#url  Unified resource locator

# def outer(name):
#     def inner():
#         print(f"Hello {name}, I am inner")
#     return inner

# outer('shaban')()

# def make_title(func):
#     def inner():
#         return func()
#     return inner

# @make_title
# def greetings():
#     return "hi there"

# print(greetings())


# def make_title(func): # we expect the function to return a string
#     def inner(name):
#         return func(name).title()
#     return inner        

# def add_mr_miss(func): # we expect the function to return
#     def inner(name):
#         return func(f"mr/Mrs. {name}")

# @make_title
# def greetings():
#     return "Hi there"

# print(greetings("fausto doe"))



# def make_title(func):
#     def inner(name):
#         return func(name).title()

#     return inner        

# def add_mr_ms(func):
#     def inner(name):
#         return  func(f"Mr/Ms. {name}")
#     return inner

# @add_mr_ms
# @make_title
# def greetings(name):
#     return name


# print(greetings("fausto doe"))




# def capitalize(name):
# #     return f'{name.title()}'

# def make_title_in_word(function):
#     def inner(name):
#        # print(name, 'inner Function')
#         return function(name).title()
#     return inner

# def add_mr(function):
#     def inner(name):
#         print(name, "line 102")
#         name = f'Mr/Mrs {name}'
#         return function(name)
#     return inner


# @add_mr
# @make_title_in_word
# def greet(name):
#     return "Good Morning " + name

# print(greet('pasco doe'))

# names =  ['peter doe', 'peer doe', 'mary doe']
# capi_names = []

# for n in names:
#     capi_names.append(n.capitalize())

# print(capi_names)

# capi_names = [ n.title() for n in names ]


# print(capi_names)

# no_ps = [ n.title() for n in names if not n.startswith('p') ]
# print(no_ps)


# names =  ['peter doe', 'peer doe', 'mary doe']

# def add_mr(function):
#     def inner(*args):
#         # full_string = ''
#         # for s in args:
#         #     full_string += s + ''
#         name = f"Mr/Mrs {' '.join([n.title() for n in args])}"
#         return function(name)
#     return inner        

# # use a decorator/closure
# @add_mr
# #@make_title_in_word
# def greet_some_humans(name):
#     # API, Test driven development
#     return "Good morning " + name    

# print(greet_some_humans('peter', 'doe', 'peer', 'mp'))


# add = lambda a, b: a + b

# print(add(1,2))

# subs = lambda c, d: c - d

# print(subs(1,2))

# divs = lambda e, f: e / f

# print(divs(1,2))

#add_string = lambda name, prefix + " " + name
# add_string = lambda prefix, name: f"{prefix} {name}"
# print(add_string('Mr', 'Pasco'))

# def capa_name(func):
#     inner =lambda name: func(name).title()
#     return inner


# @capa_name
# def greet(name):
#     return name

# print(greet('test'))

# def capa2_name(func):
#     inner =lambda *args: func(*args).title()
#     return inner

# @capa2_name
# def greet2(name):
#     return name

# print(greet2('test'))