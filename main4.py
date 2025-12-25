# l = [[1,2,3], [4,5]]
# for i in l:
#     for j in i:
#         print(j)
# for i in range(len(l)):
#     print(l[i])
# for i in range(4):
#     for j in range(4):
#         print(i, end = ' ')
#     print()
    
i = 0
while True:
    #print(i)
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    if i > 10:
        break


# a = 1
# b = 6735434 
# ls2 = [9,8,7,6]
#     0  1   2    3 
#       -3    -2     -1
#print(ls[-1])
#[start : end : step]
#print(ls[0:3:3])
# ls.append(4)
# ls.append(5)
# ls.append(5)
# ls.append(5)
# ls.append(5)
# print(dir(ls))
# print(help(ls.append))
#ls.clear()
#print(ls.count(1))
#ls.extend(ls2)
#print(ls.index(2))
#ls.insert(1 , 1)
# ls = [6,2,9,3,64,224,23,23] 
# #ls = ["A", 'b', 'c',"Dog", "Cat", "Bike", True, False, 324,3.6]
# ls2 = [[1,2,3], [4,5,"Bikes"], [7,8,9]]
# print(ls2[1][2])
# print(ls.pop())
# ls.pop()
#ls.remove(3)
#ls.reverse()
# ls.sort()
# ls.reverse()
# ls = sorted(ls)
# print(ls)
#print(ls)
#print(ls)
#print(ls)











# for i in range(6):
#     print(i , end='')
# i = 0
# while i < 10:
#     print(i, end = ' ')
#     i = i + 1

#range(start, end, step)
# print(list(range(1,5)))


#print('Allowed for voting' if int(input('Enter your age: ')) > 18 else 'Not Allowed for voting')
#print(res)

# age = int(input('Enter your age: '))
# if age > 18:
#     vid = input('Enter voter id: ')
#     print('Allowed for voting')
#     if vid == "1234":
#         print('You can vote...')
#     else:
#         print('Invalid voter id...')
# elif age == 18:
#     print('Wait 1 year to vote...')
# elif age <= 0:
#     print('Invalid age')
# else:
#     print('Not Allowed for voting')
