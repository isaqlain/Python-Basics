
# Using dummy variable called flag

inputWord = "Shaikh"
vowelGroup = ('a','e','i','o','u')
flag = 0

for eachLetter in inputWord:
    if(eachLetter in vowelGroup):
        flag = 1
        break

if(flag == 0):
    print('no')
else:
    print('yes')   
 

# Without dummy variable


inputWord = "Shaikh"
vowelGroup = ('a','e','i','o','u')

for eachLetter in inputWord:
    if(eachLetter in vowelGroup):
        print('yes')
        break
else:
    print('no')
