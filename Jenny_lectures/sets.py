# set1={5,-8,15,24,20,-5}
# print(set1)
# {20, 5, -8, 24, -5, 15}

# set11={5,-8,15,-5,24,20,-5}
# print(set11)  #no duplicate items are allowed
# {20, 5, -8, 24, -5, 15}

# set1={5,-8,15,24,20,-5}
# print(set1[2])
# TypeError: 'set' object is not subscriptable

# set1={5,-8,15,24,20,-5}
# set2=set()
# set3={}
# print(type(set1) ,type(set2),type(set3))
# <class 'set'> <class 'set'> <class 'dict'>

# set1={5,-8,15,24,20,-5}
# print(set1)
# {20, 5, -8, 24, -5, 15}
# set1.add(12)
# print(set1)
# {20, 5, -8, 24, -5, 12, 15}
# set1.remove(-8)
# print(set1)
# {20, 5, 24, -5, 12, 15}
# print(set1.pop())  #pops out any element
# 20
# print(set1)
# {5, -8, 24, -5, 15}
# set1.clear()     #clears all values
# print(set1)
# set()

# ======================================================================================

# # OPERATION ON SETS
# set1={'neeraj','stuart','happy'}
# set2={'spiderman','ironman','antman','neeraj'}
# set3={'captain america','hawkeye','neeraj','stuart'}

# print(set1.union(set2))
# {'happy', 'antman', 'spiderman', 'neeraj', 'stuart', 'ironman'}
# print(set1.union(set2,set3))
# {'ironman', 'happy', 'antman', 'hawkeye', 'stuart', 'neeraj', 'captain america', 'spiderman'}
# print(set1 | set2)
# {'happy', 'antman', 'spiderman', 'neeraj', 'stuart', 'ironman'}
# print(set1 | set2 | set3)
# {'ironman', 'happy', 'antman', 'hawkeye', 'stuart', 'neeraj', 'captain america', 'spiderman'}
# print(set1.union(('hello', 'world')))
# {'hello', 'happy', 'world', 'neeraj', 'stuart'}

# set1.update(set2)
# print(set1)
# {'happy', 'ironman', 'spiderman', 'neeraj', 'antman', 'stuart'}

# set1.update(['hello','world'])
# print(set1)
# {'neeraj', 'stuart', 'hello', 'world', 'happy'}

# print(set1.intersection(set2))
# {'neeraj'}
# print(set1.intersection(set3))
# {'neeraj', 'stuart'}
# print(set1.intersection(set1,set3))
# {'neeraj'}
# print(set1 & set2)
# {'neeraj'}

# print(set1.difference(set3))
# {'happy'}
# print(set1 - set2)
# {'stuart', 'happy'}

# set1.difference_update(set2)
# print(set1)
# print(set2)
# {'happy', 'stuart'}
# {'neeraj', 'antman', 'ironman', 'spiderman'}

# print(set1.symmetric_difference(set2))
# {'spiderman', 'stuart', 'ironman', 'antman', 'happy'}
# print(set1 ^ set2)
# {'spiderman', 'stuart', 'ironman', 'antman', 'happy'}
# print(set1 ^ set2 ^ set3)
# {'antman', 'happy', 'neeraj', 'spiderman', 'captain america', 'ironman', 'hawkeye'}

# set1.symmetric_difference_update(set2)
# print(set2)
# {'ironman', 'neeraj', 'spiderman', 'antman'}


# set1={1,2,3,4,5}
# set2={20,5,12,2,3,-7,4,1}
# set3={20,12,-7}

# print(set1.isdisjoint(set3))
# True
# print(set1.issubset(set2))
# True
# print(set1.isdisjoint(set2))
# False
# print(set1.issubset(set2))
# True
# print(set2.issubset(set1))
# False

#  we can use >= for superset and <= for subset 