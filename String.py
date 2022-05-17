 
 
 
 # Example 1
  
myStr = 'pythonon'
abc = myStr.count('p')
print(abc)
# Output: 1


 # Example 2
find() - It will return the index of the first occurance 
myStr = 'pythonon'
abc = myStr.find('o')
print(abc)
# Output: 4

 # Example 3
rfind() - It will return the index of the first occurance element from right side
myStr = 'pythonon'
abc = myStr.rfind('o')
print(abc)
# Output: 4


# Example 4
index() - It will return the index of the first occurance element
myStr = 'pythonon'
abc = myStr.index('o')
print(abc)
# Output: 4

# Difference between find() & index()

index() - It cannot be used with conditional statement
find() - It can be used with conditional statement to execute a statement if a substring is found as well if it is not

# Example 5

abc = 'apple'
print('zz',abc,'yy')
zz apple yy
abc = abc.strip()
print('zz',abc,'yy')

# Output: zz apple yy

# Example 6

abc = 'apple'
abc = abc.strip('e')
print(abc)

# Output: appl

# Example 7
abc = 'applea'
abc = abc.strip('a')
print(abc)
# Output: pple

# The strip() function will only remove whitespaces before start and after end but not in between also if we pass the argument then it will remove that element also.

# The split() function will return all the individual elements in a list format. If we pass argument of existing letter then it will cut the string into 2 parts from that point except that letter.

# To remove all the whitesapces contained in a string make use of replace() function

"  hello  apple  ".replace(" ", "")
'helloapple'

If you want to remove duplicated spaces, use str.split() followed by str.join():

>>> " ".join("  hello  apple  ".split())
'hello apple'

# Example 8

abc = 'apple'
ghi = max(abc)
print(ghi)
#Output: p

# Example 9

abc = 'apple'
ghi = min(abc)
print(ghi)
#Output: a

# Example 10

abc = 'apple'
ghi = len(abc)
print(ghi)
#Output: 5

# Example 11

abc = 'apple'
ghi = min(abc)
print(ghi)
#Output: a

# Example 12
ghi = abc.replace('p','z')
print(ghi)
# Output: azzle






