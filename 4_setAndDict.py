myDict = {1: 1, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 1: 3}
print(myDict)
print(myDict[1])
print(myDict.get(1))
print(6 in myDict)
print(myDict.get('1'))

mySet = set([1, 1, 2, 2, 2, 3, 3, 4, 5])
print(mySet)

mySet2 = set([2, 3, 7])
print(mySet & mySet2)
print(mySet | mySet2)
