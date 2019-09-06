# for i in range(100):
#     print('this is line {}'.format(i))

# def f1():
#     print('...')
#     return 1
# # f1()
# # print(f1())
# # print(f1)
# f2=f1
# f2()
# f2=f1()
# f2()

# def f2(a,b):
#     return a+b
# print (f2(1.1,3))
# print(f2('ab','c'))
# print(f2('abc',123))

d1 = {'a': 'apple', 'b': 'boy', 'c': 'cat', 'd': 'dog'}
d1
d1.items()
d1.keys()
d1.values()
d1['a']
d1['e'] = 'egg'
for k, v in d1.items():
    print(k, "=", v)
