

#lists dict
#any & all


# print(all((0,0)))

# print(all((0,1)))

# print(all(("","")))

# print(all("c"))

# print(all((1,1)))

# print(all((None, "is", "awe")))

# print(any((None, "is", "awe")))

# netflix_sub = [
#     {"name": "Fausto", "paid": False},
#     {"name": "Pasco", "paid": True},
#     {"name": "Emily", "paid": False},
# ]

# paid = []
# for user in netflix_sub:
#     if user["paid"]:
#         paid.append(user)

# print(len(paid), len(netflix_sub))
# have_all_paid = len(paid) == len(netflix_sub):
# print(have_all_paid)
# paid = []
# for user in netflix_sub:
#     paid.append(user['paid'])
# have_all_paid = all(paid)

# have_all_paid = all([user['paid'] for user in netflix_sub])
# print(have_all_paid)

    # if have_all_paid:
    #     print(True)
    # else:
    #     print(False)


# print(all((None, "is", "awesome")))
# print(any((None, "is", "awesome")))


# netflix_subscribers = [
#     {"name": "Fausto", "paid": False},
#     {"name": "Jacque", "paid": False},
#     {"name": "Pasco", "paid": False},
#     {"name": "Wessam", "paid": False},
#     {"name": "Emily", "paid": False},
# ]



# paid = []
# for user in netflix_subscribers:
#     if user['paid']:
#         paid.append(user)
# # logic @ boolean 
# print(len(paid), len(netflix_subscribers))
# have_all_paid = len(paid) == len(netflix_subscribers)

# have_all_paid = all([u['paid'] for u in netflix_subscribers])


# names = ['jac doe', 'peer doe', 'miri doe', 'shaban doe']

# all_names_capitalize = []
# for name in names:
#     all_names_capitalize.append(name.capitalized())

# map(<function>, <iterable>)
# all_names_capitalize = map(lambda name: name.capitalize(), names)

# all_names_capitalize = map(lambda name: name.title(), names)
# #all_names_capitalize = map(str.title(), names)
# print(list(all_names_capitalize))

# def capitalize(name):
#     return name.capitalize()


# all_names_capitalize = map(capitalize, names)

# print(list(all_names_capitalize))


#filter
# names = ['reiner', 'peter', 'john']

# # for name in names:
# #     if name.endswith('er'):
# #         names.remove(name)
# # print(names)

# names1 = filter(lambda name: not name.endswith('er'),names)
# print(names)
# print(list(names1))


#names = ['jacque doe', 'peer doe', 'mirjam doe', 'shaban doe']


#names = [{'name': 'jacque doe'}, {'name': 'peer doe'}, {'name': 'mirjam doe'}, {'name': 'shaban doe'}]

# all_names_capitalize = map(lambda name: name.title(), names)


# names = filter(lambda name: not name.endswith('er'), names)

# names1 = filter(lambda name: not name.endswith('ue'),names)
# print(names)
# print(list(names1))
# def filtering_jac(name_dict):
#     if name_dict['name'].startswith('jacque'):
#         return False
#     return True

# names = filter(lambda name_dict: not name_dict['name'] != 'jacque', names)
# print(list(names))

# names = filter(lambda name_dictionary: not name_dictionary['name'].startswith('jacque'), names)
# print(list(names))