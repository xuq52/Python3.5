print(abs(-100))  # 绝对值
print(max(1, 3, 8, -1))
print(hex(255))  # hex()将整数转换为16进制数

# 定义函数


def my_abs(x):       # 参数x要写
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


def nop():  # 定义空函数
    pass

# if age >=18:
 #   pass
# 试试my_abs和内置函数abs的差别：???


def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs1(5))
# print(my_abs1('a'))

import math


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi/6))

import math


def quadratic(a, b, c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2


print(quadratic(1, 3, 1))


def power(x3):
    return x3*x3
print(power(4))


def power1(x4, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x4
    return s
print(power1(3,3))

def power2(x5,n=3):
    s1=1
    while n>0:
        n=n-1
        s1=s1*x5
    return s1
print(power2(5))

def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum +n*n
    return sum
print(calc([1,2,3]))
print(calc([5]))

def calc1(*numbers):
    sum1=0
    for n1 in numbers:
        sum1=sum1 +n1*n1
    return sum1
print(calc1(1,2,3))
print(calc1(5))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other',kw)
print(person('mickael',30))
