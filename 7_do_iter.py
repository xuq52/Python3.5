from collections.abc import Iterable
d = {1: '11', 2: '22', 3: '33'}
for key in d:
    print(key)

for value in d.values():
    print(value)

for a in 'abs':
    print(a)

print(isinstance('123', Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
