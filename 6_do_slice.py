L = ["a", "b", "c", "d", "e"]
print(L[:3])
#['a', 'b', 'c']
print(L[-2:])
#['d', 'e']
L1 = list(range(100))
print(L1[:10])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L1[::5])
#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print(L1[:10:2])
#[0, 2, 4, 6, 8]
print("ABCDEFG"[::2])
# "ACEG"


def trim(s):
    if(len(s) == 0):
        return ""
    while (s[0] == " "and len(s) != 1):
            s = s[1:]
    while (s[-1] == " " and len(s) != 1):
        s = s[:-1]
    if(s[0]==" " and len(s)==1):
        return ""
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
