
myWord = "My name is anu"
vowel = ('a','e','i','o','u')

wordSplit = myWord.split()

start = []
end = []
startAndEnd = []

for word in wordSplit:
    if(word[0] in str(vowel)):
        start.append(word)
        
    if(word[-1] in str(vowel)):
        end.append(word)

    if(word[0] in str(vowel) and word[-1] in str(vowel)):
        startAndEnd.append(word)

print(start)
print(end)
print(startAndEnd)
    
