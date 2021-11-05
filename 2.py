
# l = list() # []
# l.append(10)
# l.append(-3)
# l.append(25)
# l.append("asdn123")
# l.append([1, 2, 3 ,4])
# l.sort()
# l.reverse()
# print(l.pop())
# print(l)

# t = tuple([10, -3, 5])
# print(t.count(-1))

# t = ("s", )
# print(type(t))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# s = "hello"
# print("hell" in s)

# print(hash('abcdef'))
# print(hash('abcdee'))

# d = dict(a='1234', b='5678')
# {
#     'a': 1234,
#     'b': 5678,
# }
# s = {1, 2, 3, 5, 4}
# print(s)
# print(2 in s)

# a = 31244
# b = 31244
# print(a is b)
# # print(id(321))

# l1 = [1, 2, 3, 4, 5]
# l2 = l1.copy()
# l2.append(10)
# print(l1)
# print(l2)
# print(l1 is l2)
# print(l1 == l2)

# if 10>11:
#     print("True")
# else:
#     print("False")

# is_valid = True
# status = 'clean' if is_valid else 'not clean'
# print(status)
# print(int(is_valid))
# status = ('not clean', 'clean')[is_valid]
# print(status)

# func_output = None
# msg = func_output or 'No output'
# print(msg)

# if result == 1:
#     print('Good')
# elif result == 2:
#     print('Bad')

# i = 10

# while i>0:
#     print(i)
#     i-= 1

l1 = {
    'a' : [1, 2, 3, 4, 5],
    'b' : 4321
}
for x in "1234556":
    if x in ('sds'):
        break
    print(x)
else:
    print('не был')
print('end')

