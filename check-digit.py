# In this program we checked whether the given digit is present or not.
# key points is that integer is not iterable so we need to convert it into str type


checkDigit = 8
output = []
myList = range(1,101)

for eachDigit in myList:
    if(str(checkDigit) in str(eachDigit)):
        output.append(eachDigit)

print(output)
        
