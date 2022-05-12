mySentence = "My name is Shaikh"
wordsSplit = mySentence.split()

# Why we are taking vowel as tuple instead of string
vowel = ('a','e','i','o','u')
start = {}


for word in wordsSplit:
    count = 0
    for eachWord in word:
        if(eachWord in  str(vowel)):
            count = count + 1
            start[word] = count

print(start)
        
        
  
