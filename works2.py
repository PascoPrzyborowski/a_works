


#Dictionary
# Container of information with key / value pairs

#mutable and fast
#0(1) in runtime all functions
#

from struct import unpack

from regex import F


fruit_col = {
    "apple": "red",
    "berries": "blue"
    #"another_Dict": {"a":"letter"} # nested dict
}

#print(fruit_col["apple"])

#print(fruit_col["not exist"]) # KeyError

#print(fruit_col.get("X", "not there in dict")) # default Errormsg if not in Dict

# loop/ iterate over Dict

# for key in fruit_col:
#     print(key)
#     print(f"The color of {key} is {fruit_col.get(key)}") # {} key, .get() Val of key


# print(fruit_col.values()) # Vals of dict
# for v in fruit_col.values():
#     print(v)

# print(fruit_col.items()) # list of key/vals [(key,val)] of all items in dict
# for a_t in fruit_col.items():
#     print()
#     print(a_t)
#     #unpack
#     x, y = a_t
#     print(x)
#     print(y)
#     print("=" * 10)

# def dict_all_in(fruit_col):
#     for key in fruit_col:
#         print()
#         print("Keys: ")
#         print(key)
#         print(f"The color of {key} is {fruit_col.get(key)}") # {} key, .get() Val of key
#         print("=" * 10)
#     for v in fruit_col.values():
#         print()
#         print("Values: ")
#         print(v)
#         print("=" * 10)
#     for a_t in fruit_col.items():
#         print()
#         print("Items: ")
#         print(a_t)
#     #unpack
#         x, y = a_t
#         print(x)
#         print(y)
#         print("=" * 10)

# dict_all_in(fruit_col)

#puzzle
# del keys

# d = {
#     "soccer": "lpay with foot",
#     "paddle": "Fake tennis",
#     "poker": "played in Vegas"
# }

# for key in d.fromkeys(d.keys(), ' '):
#     if key.endswith('er'):
#         del d[key]
# print(d)

# for key in d.copy(): # make Dict in list
#     if key.endswith('er'):
#         del d[key]
# print(d)


# for key in list(d): # make Dict in list
#     if key.endswith('er'):
#         del d[key]
# print(d)


# d = {"key":{"a": 2}}
# print(d["key"]["a"])
# d.setdefault("b":999) #set "b" it if not exist and give value 999 by default,  careful Use change vals!!
# #get only give an Error if not exist

#d.update({"a": 3}) # add val, carefull overwrite val  from a if exist !!
#d.popitem({"z": 999}) #remove last from dict manuell, careful !! 

list_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

# count = 1
# for day in enumerate(list_days):
#     print(day)
# #    print(f"{day} is day {count}")

# #    x       y
# for index, day in enumerate(list_days):
#     print(f"{day.capitalize()} is day {index + 1}")
#    # print(day)

# for index, day in enumerate(list_days, start=1):
#     print(f"{day.capitalize()} is day {index }")

#zip combine two iterabeles to one combined object

# x = [1,2,3]
# y = ["a", "b", "c"]
# z = zip(x, y)
# #print(z)
# for i in z:
#     print(i)
# print()

# x = [1,2,3,4]
# y = ["a", "b", "c","d","e"] 
# p = ["x", "y", "z","q"]
# z = zip(x,y,p)
# # d = dict(z)
# print(z)
# for i in z:
#     print(i)
# print()
#print(d)


# x = [1,2,3,4]
# y = ["a", "b", "c","d","e"] 

# for a, b in zip(x, y):
#     print(a, b)
# print()
# for index, value in enumerate(x):
#     print(y[index], value)
# print()
# for j in zip(x,y):  # zip are tuple (a, b)
#     print(j)
# print()

#max min
# numbers = [3,1,2,4,100,5]

# max_val = 0
# for n in numbers:
#     if n < max_val:
#         max_val = n
# print(max_val)

# max_val = max(numbers)
# print(max_val)

# min_val = min(numbers)
# print(min_val)

# words = ["apple", "aaaapple", "cat", "caaaat"]
# print(max(words))
# print(min(words))

# numbers = [4,3,2,1]
# #numbers.sort() # to a var = none!! change it
# # sorted(numbers) # sorts and returns but don't change orginal num until var
# # print(numbers)
# numbers = sorted(numbers, reverse=True)
# print(numbers)

# sorted for dict too by keys or values
# d = {"a": 1, "c": 3, "b": 2 }

# books = {
#     {"cost": 1, "title": "Python 2"}
# }
# # print(sorted(books, key=lambda book: book['cost']))

# func = lambda book: book['cost']
# print(sorted(books, key= func))


books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# readable!
func = lambda book: book['cost']
print(sorted(books, key=func))
print()

func = lambda book: book['cost']
print(sorted(books, key=func, reverse=True))
print()


# numbers = sorted(numbers, reverse=True)
func = lambda book: book['name']
print(sorted(books, key=func))
print()

func = lambda book: book['name']
print(sorted(books, key=func, reverse=True))
print()

