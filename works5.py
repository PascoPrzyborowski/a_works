
#equal or not equal

# list1 = [32,32,32,32,32,32,32,32,]
# #v = list1[0]

# for element in list1:
#     if list1[0] != element:
#         print('no not all same')
#         exit()
# print('yes all same')



#search
# list1 = [2,3,1,9,8,7]
# #print(list1.index(1))

# looking_for = 8

# for element in list1:
#     if element == looking_for:
#         print('found digit')
#         exit()
# print('not found digit')



#Scopes inside out a function
# x = 4
# y = 6

# l = []
# d ={}

# def f():
#     x = 5
#     if x > 3:
#         z = 9
#         print(z)

# print("inside x val f")
# f()
# print("outside x val f")
# print(x)



#Re use Function

# l1 = [1,2,3]
# l2 = [4,5,6,]

# def f (lst):
#     for item in lst:
#         print(item)

# l = []
# for i in range(5):
#     l.append(int(input('Type num: ')))

# f(l)



# products = [
#     {
#         'name': 'sofa',
#         'price': 350,
#         'qnt': 4
#     },
#     {
#         'name': 'table',
#         'price': 50,
#         'qnt': 5
#     }
# ]

# def search_product(k, qnt=1):
#     for product in products:
#         if product['name'] == k and product['qnt'] >= qnt:
#             print('yes we have!')
#             print(f'It costs {product["price"]}!')
#             return
#     print('no we have not')


# keyword = input('What Sofa do You search:')
# quand = int(input('product quantity:'))

# search_product(keyword, quand)

# keyword = input('What Table do You search:')
# quand = int(input('product quantity:'))
# search_product(keyword,quand)



def f (x):
    return x+1

print(f(2))

