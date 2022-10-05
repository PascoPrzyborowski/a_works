

# transformer = ['a', 'u', 't', 'o', 'b', 'o', 't', 's']

# print(transformer)
# # str1 = ""
# # str1.join(['a', 'u', 't', 'o', 'b', 'o', 't', 's'])
# print("".join(transformer))
# # print(str1)


# lists = [["John",["Mary"], "Amy"],["32","43","51"]]
# print(lists[0][1][0])

# lists = [["John",[{"name":"Mary"}], "Amy"],["32","43","51"]]
# print(lists[0][1][0]["name"])

# seq = range(1,5,2)
# print(seq)
# print(list(seq)) 
# s = range(1,5)
# list(s)
# print(s)
# print(list(s))


# sizes = ("s","m","l","xl","10")

# for i in range(len(sizes)):
#     print(i)sizes

# for s in range(sizes):
#     print(s)

# sizes = ["s","m","l","xl","10"]
# print(sizes)
# print(sizes.index('m'))
# print(sizes.count('m'))
# #print(sizes.append('0','p'))

# alpha = ['a','b','c','d']
# print(alpha)
# print(alpha[::-1])
# print(alpha[::-2])
# print(alpha[::2])
# alpha.reverse()
# print(alpha)

# num = [4,3,2,100,0]
# num.sort()
# print(num)

#
# words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
# words.sort()
# print(words)
# # words = words.sort()
# # print(words)
# words.sort(reverse=True)
# print(words)

# words[0] = "rat"
# words[0:2]= "lion"
# print(words)
# words[0:2]= ["lion"]
# print(words)
# words.remove('o')
# words.remove('n')
# print(words)

# words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
# print(words)
# words[1]= "Lion"
# words[3]= "Lion"
# print(words)

# words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
# print(words)
# words[1:3]= ["Lion"]
# print(words)
# words[0]=None
# print(words)
# words.append('last')
# print(words)
# list_a=[1,2,3]
# list_b=[4,5,6]
# print(list_a)
# print(list_b)
# print(list_a + list_b)

# list_a=[1,2,3]
# list_b=[4,5,6]
# list_a.extend(list_b)
# print(list_a)

# alpha = ['a','b','c']
# print(alpha)
# alpha.insert(1, 'x')
# print(alpha)
# alpha.pop()
# print(alpha)
# alpha.pop(1)
# print(alpha)
# #help(alpha.pop)

# alpha = ['a','b','c']
# print(alpha)
# alpha.remove('c')
# print(alpha)

# a = [1,2,3,]
# b = [1,2,3,]
# c = [3,2,1,]

# print(a == b)
# print(a == c)

# name = "Pasco"
# name = tuple
# name = tuple("Pasco")
# print(type(name))
# print(name)
# print(type(name))

#mixed datatypes in Tuple Possible !!
#tuple not mutable

# food = (
#     ('tuna', 'salomon'),
#     ('apples','oranges')
# )

# print(food)


# somet = ('a','b','c')

# print(somet.index('c'))
# print(somet.count('c'))

# x = ([],)
# x[0].append("ha")
# print(x)   

# print(tuple([1,2,3]))

# tuple only index and count

# l1 = ([1,2,3])
# l2 = ([1,2,3])
# print(sorted(l2, reverse = True))
# print(l1 == l2)

# print(l1 is l2)

#set

# food = {"Salmon","Codd","Grapes"} # food full set  food empty dict
# print(food)
# print(type(food))

# name = "Lucas Schertel"
# # print(set(name))

# counter = {}
# name = name.lower()
# set_of_name = set(name)
# for letter in set_of_name:
#     print(name.count(letter),letter)

# counter ={}
# for letter in set_of_name:
#     counter[letter] = counter.get(letter, 0) +1

# print(counter)

# name = "Lucas Schertel"
# name = name.lower() 
# #print(name)

# # counter = {}
# # counter.setdefault()

# # duplicate = "hellloooo"
# set(name)
# # print(set(duplicate))
# counter = {}
# for key in name:
#     counter.setdefault(key, name.count(key))


# print(counter)

# dedub with a word

# word = "this word has many words"
# counts = {}
# for char in word.lower():
#     counts.setdefault(char, 0)
#     counts[char] = counts[char] + 1

# counts = {}
# for char in set(word.lower()):
#     counts.setdefault(char, 0)
#     counts[char] = counts[char] + 1

# print(counts)




# dub = ("app","app","app","bap")
# print(set(dub))

# # loc = ('Berlin', 'London','Paris')
# # copy_loc = loc.copy

# print(loc)
# print(copy_loc)


# loc = {"Berlin"}
# print(loc)
# loc.add('London')
# print(loc)
# loc1 = {"Madrid"}
# loc.update(loc1)
# print(loc)


# loc = {"Berlin"}
# print(loc)
# loc.add('London')
# print(loc)
# loc1 = ["Madrid"]
# loc.update(loc1)
# print(loc)

# #set.pop (last out of list)
# #set.discard (none)
# #set.remove (can crash)
# #set.clear (good but all)




# loc = {'Berlin', 'London','Paris', 'Stockholm'}
# #loc.pop()
# # loc.remove('Berlin')
# # loc.remove('Berlin')# mistake
# #loc.discard('Berlin')# good
# #loc.discard('London')# good
# #loc.clear() # clear all
# print(loc)


#intersection

# set1 = {1,2,3,4,}
# set2 = {4,5,6,7,}

# print(set1.intersection(set2)) #only common dub on set1 and set2
# print(set1,set2)
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1 - set2)

# print(set1.symmetric_difference(set2))
# print(set1.__xor__(set2)) # all without common item

#all functions with update to update
# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1, set2)

# print(set2.intersection(set1))
# set2.intersection_update(set1)
# print(set1, set2)
# print(set1.union(set2)) # all numbers without dub common items but common in too
# print(set1)
# print(set2)



# set1 = [1,2,3,4,]
# set2 = [4,5,6,7,]
# print(set1 + set2)

# A = {1,2,3,4,}
# B = {4,5,6,7,}
# print(A,B)
# print(A.isdisjoint(B))

# C = {1,2,3,} # nothing in common
# D = {4,5,6,7,}
# print(C,D)
# print(C.isdisjoint(D))


# A = {1,2,3,4,5,6,7,}
# B = {1,2,3,4,5,6,7,}
# print(A,B)
# print(A.issubset(B))

# C = {1,2,3,} # nothing in common
# D = {4,5,6,7,}
# print(C,D)
# print(C.issubset(D))


# A = {1,2,3,4,5}
# B = {4,5,}
# print(A,B)
# print(A.issuperset(B))

# C = {1,2,3,} # nothing in common
# D = {4,5,6,7,}
# print(C,D)
# print(C.issuperset(D))




# l1 = [1,2,3,] #list
# l2 = [1,2,3,]
# s1 = {1,2,3} #set
# s2 = {1,2,3}
# t1 = (1,2,3) #tuple
# t2 = (1,2,3)

# print(l1 == l2)
# print(s1 == s2)
# print(t1 == t2)