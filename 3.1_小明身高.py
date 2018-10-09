n=80.5/1.75/1.75
if n<18.5:
    print('过轻')
elif n>18.5 and n<25:
    print('正常')
elif n>25 and n<28:
    print('过重')
else:
    print('肥胖')