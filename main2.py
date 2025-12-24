
# print(help(yield))
# from functools import reduce
# l = [(1,3,4), (5,2,6), (9,1,3)]
# l.sort(key=lambda x: x[1])
#print(l)
# Functions
# l = [8,4,6,8,2,1]
# age = 18
# if all([age == 18,age == 18 ,age == 18]):
#     print('Success')
#print(l)




# Reduce
# def mul(x,y):
#     return x*y
# def reduce2(func, ls):
#     prev = 1
#     for i in ls:
#         prev = func(prev, i)
#     return prev
# res = reduce2(lambda x,y: x*y, l)
# Filter
# def cmp(x):
#     return x%2 == 0

# def filter2(func, ls):
#     res = []
#     for i in ls:
#         if func(i):
#             res.append(i)
#     return res
# print(list(filter2(lambda x: x%2 != 0, l)))




# map
# def map2(func, ls):
#     for i in range(0, len(ls)):
#         ls[i] = func(ls[i])
#     return ls




# for i in range(0, len(l)):
#     l[i] *= l[i]
# def sq(x):
#     return x**2
# new_l = list(map(lambda x : x**2, l))
#print(map2(lambda x : x*2, l))





# def sum(x,y):
#         return x+y
# def sq(x):
#         return x*x

# sq2 = lambda x: x**2
# print(sq(5))
# print(sq2(6))
# sum2 = lambda x,y: x+y
# print(sum(3,4))
# print(sum2(3,4))

# age = 18
# if age < 18:
#     print('Not Eligible')
# else:
#     print('Eligible')
# var = 'Not Eligible' if age < 18 else 'Eligible'
# print('Not Eligible' if age < 18 else 'Eligible')
#print(var)
# def Fun(x, *args, **kwargs):
#     print(x)
#     print(args)
#     print(kwargs.values())

# Fun(5, 6,7,8,name='python', year=2025, age=45)


# def add(*args):
#     # sum = 0
#     # for i in args:
#     #     sum += i
#     return sum(args)

# print(add(5,6,7,7,8,9))



# def mul(x,y):
#     return x*y

# def Operations(fun, x,y):
#     return fun(x,y)

# print(Operations(mul, 3,2))


# def fun():
#     print("hello")
# def sum(x,y):
#     print(x+y)
# sum(4)

# def Welcome(name, message="Hello"):
#     print(message + " "+ name)
# Welcome("Python","Hi")

# def mul(ls):
#     res = 1
#     for i in ls:
#         res *= i
#     return res
# print(mul([1,2,3,4]))


# # dist = {}
# # print(help(len))



# dist = {
#     "Name":"Python",
#     "Number":25,
#     34:1,
# }
# dist2 = {
#     "Reg_no":"8575"
# }
# dist.update(dist2)
# print(dist)
# print(dist.get('3'))
# print(dir(dist))
# dist2 = {}
# dist2['Name'] = 'Hello'
# dist2['Name'] = 'Python'
# dist2['5'] = 'Python'
# dist2['6'] = 'Python'
# dist2['6'] = 'Python'
# dist2.pop('Name')
# dist2.popitem()
# dist2.clear()
# dist3 = dist2.copy()
# dist3['6'] = '6'
# print(dist2)
# print(dist3)

# for i,j in dist2.items():
#     print(i + " " + j, end = '\n')

#print(len(dist2))
# if "Name" in dist2:
#     print(dist2["Name"])