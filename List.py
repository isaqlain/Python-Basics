# Example 1

abc = ['aa','bbb','ccc']
sep = '-'
ghi = sep.join(abc)
print(ghi)

# Example 2

myList = [11,22,33,11,22,33]
myLen = len(myList)
print('myLen:',myLen)

# Example 3

myList = [11,22,33,11,22,33]
myLen = min(myList)
print('myLen:',myLen)

# Example 4

# count attr of list will count the occurances of element in the list

myList = [11,22,33,11,22,33]
myLen = myList.count(11)
print('myLen:',myLen)

# Output myLen: 2

# Example 4

myList = [11,22,33,11,22,33]
myLen = myList.count(11)
print('myLen:',myLen)

# Example 5

# index attr of list will return occurence of passed element

myList = [11,22,33,11,22,33]
myLen = myList.index(11)
print('myLen:',myLen)

# output myLen: 1

# Example 6

myList = [11,22,33,11,22,33]
myList.append('apple')
print('myLen:',myList)

# Output [11, 22, 33, 11, 22, 33, 'apple']

# Example 7

myList = [11,22,33,11,22,33]
myList.extend('orange') # it will extract individual element and add it to the list
print('myLen:',myList)

# Output [11, 22, 33, 11, 22, 33, 'apple', 'o', 'r', 'a', 'n', 'g', 'e']

# Example 8

myList = [11,22,33,11,22,33]
secList = ['abc','ghi']
myList.append(secList) # it will add the list to the last
print('myLen:',myList)

# Output myLen: [11, 22, 33, 11, 22, 33, ['abc', 'ghi']]

# Example 9

myList = [11,22,33,11,22,33]
secList = ['abc','ghi']
myList.extend(secList) # it will extract each element and will add to the list
print('myLen:',myList)

# Output myLen: [11, 22, 33, 11, 22, 33, ['abc', 'ghi'], 'abc', 'ghi']

# Example 10

myList = [11,22,33,11,22,33]
secList = ['abc','ghi']
myList.insert(1,'secList') # it will add the element at position 1
print('myLen:',myList)

# Output myLen: [11, 'secList', 22, 33, 11, 22, 33, ['abc', 'ghi'], 'abc', 'ghi']

# Example 11

myList = [11,22,33,11,22,33]
secList = ['abc','ghi']
myList.insert(1,secList) # it will add the list at position 1
print('myLen:',myList)

# Output myLen: [11, ['abc','ghi'], 22, 33, 11, 22, 33, ['abc', 'ghi'], 'abc', 'ghi']

# Example 12

myList = [11,22,33,11,22,33]
del(myList)
print('myLen:',myList)

# Example 13

myList = [11,22,33,11,22,33]
myList.pop() # It return and remove the last element
print('myLen:',myList)

# Output myLen: 33

# Example 14

myList = [11,22,33,11,22,33]
myList.pop(2) # It return and remove the element at position 2
print('myLen:',myList)

# Output myLen: 33

# Example 15

myList = [11,22,33,11,22,33]
myList.remove(22) # It return and remove the element 22
print('myLen:',myList)

# Output myLen: 33

# Example 15

myList = [11,22,33,11,22,33]
myList.reverse() # It reverse the list
print('myLen:',myList)

# Output myLen: [33, 22, 11, 33, 22, 11]

# Example 16

myList = [11,22,33,11,22,33]
myList.sort() # It sort the list in ascending order
print('myLen:',myList)

# Output myLen: [33, 22, 11, 33, 22, 11]
