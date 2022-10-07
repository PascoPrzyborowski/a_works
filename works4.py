#collections



# fridge = [
#  "Apple", "Apple", "Cabbage",
#  "Steak", "Cheese", "Apple",
#  "Carrot", "Carrot", "Iogurt",
#  "Beer"
# ]

# counter = {}

# for ingredient in fridge:
#     if ingredient not in counter:
#         counter[ingredient] = 0
#     counter[ingredient] += 1

# print(counter)


# from collections import Counter

# fridge = [
#  "Apple", "Apple", "Cabbage",
#  "Steak", "Cheese", "Apple",
#  "Carrot", "Carrot", "Iogurt",
#  "Beer"
# ]

# counter = Counter(fridge)

# print(counter)

#print(counter.total())

# from collections import OrderedDict

# a_dict = {"name": "Mary Schmidt", "age": 54, "height": 120}

# ordered = OrderedDict(a_dict)

# print(ordered)

# ordered.move_to_end("age", last=False)

# print(ordered)


# from collections import ChainMap

# prices_1 = {"creme_egg": 2 }

# prices_2 = {"creme_egg": 3 }

# chain = ChainMap(prices_2, prices_1)

# print(chain)

# print(dict(chain))

# print(chain["creme_egg"])


# from collections import ChainMap

# prices_1 = {"creme_egg": 2, "curly_wurly": 2 }

# prices_2 = {"creme_egg": 3 }

# prices_3 = {"creme_egg": 5 }

# chain = ChainMap(prices_3, prices_2, prices_1)

# print(chain)

# print(dict(chain))

# print(chain["creme_egg"])

# #print(chain.maps)

# from collections import ChainMap

# tesco_prices = {"creme_egg": 2, "curly_wurly": 2 }

# m_s_prices = {"creme_egg": 5, "curly_wurly": 4 }

# chain = ChainMap(tesco_prices)

# chain_2 = ChainMap(m_s_prices, chain)

# print(chain_2)

# from collections import namedtuple

# Address = namedtuple('Address', ['street', 'number', 'city', 'county'])

# home = Address("Private Drive", 4, "Little Whinging", "Surrey")

# print(home)

# from collections import namedtuple

# # configuration of our named tuple
# Address = namedtuple('Address', ['street', 'number', 'city', 'county'])

# # use it
# myAddress = Address("Private Drive", 4, "Little Whinging", "Surrey")

# yourAddress = Address("Some road", 24, "Wateg", "Someplace")

# print(home)

# from collections import namedtuple

# # configuration of our named tuple
# Address = namedtuple('Address', ['street', 'number', 'city', 'county'])

# # use it
# myAddress = Address("Private Drive", 4, "Little Whinging", "Surrey")

# yourAddress = Address("Some road", 24, "Some city", "Some County")

# print(yourAddress.city)


# from collections import namedtuple

# # configuration of our named tuple
# Address = namedtuple('Address', ['street', 'number', 'city', 'county'])

# # use it
# my_address = Address("Private Drive", 4, "Little Whinging", "Surrey")

# your_address = Address("Some road", 24, "Some city", "Some County")

# print(your_address._asdict())

# new_your_address = your_address._replace(city="Some New City")

# print(new_your_address)
# print(your_address)





