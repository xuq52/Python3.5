import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-2323))


def multiReturn(x, y):
    return x+1, y+1


x, y = multiReturn(1, 2)
print(x, y)


def power(x, n=2):
    s = 1
    while n > 0:
        s = s*x
        n = n-1
    return s


print(power(5))
print(power(5, 3))

# 默认参数必须指向不可变参数


def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())


def cal(*num):
    s = 0
    for n in num:
        s += n
    return s


print(cal(1, 2, 3))
nums = [1, 2, 3, 4]
print(cal(*nums))
nums = (1, 2, 3)
print(cal(*nums))


def printInfo(name, sex, **other):
    print('name:', name, ' sex:', sex, 'other:', other)


other = ['vv', 'dd']
printInfo('aa', 'bb', other=other)
other = {'vv': 'vv', 'dd': 'dd'}
printInfo('aa', 'bb', **other)

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def person(name, age, *, city, job):
    print(name, age, city, job)

person('1','2',city='123',job='123')

def person1(name,age,*other,city,job):
    print(name,age,other,city,job)

person1('1','2',*[1,2,3,4],city='123',job='123')

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
