import array as arr

a = arr.array('b', [1,2,3,4])
print(a)

#we can remove or pop element by index using pop() method

a.pop(2)
print(a)

a.pop(2)
print(a)

a.insert(2,7)
a.insert(2,8)
print(a)

#we can also delete element by index using del command

del a[2]
print(a)

del a[2]
print(a)