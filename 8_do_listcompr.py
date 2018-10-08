import os
print(len('速秀霖                                               '))
print(list(range(1, 10)))
print(list(x*x for x in range(1, 10)))
print(list(x*x for x in range(1, 11) if x % 2 == 0))
print(list(m+n for m in 'ABC' for n in '123'))

print([d for d in os.listdir('.')])

d={'1':'A','2':'B','3':'C'}
print([k+'='+v for k,v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]

L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 1111
# 这是我老公教我的