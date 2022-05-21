abc = 10
while(abc<20):
    if(abc == 14):
        continue
    if(abc == 12):
        break
    abc = abc + 1
    print(abc)
    
  
  # 2
  
  while(abc < 20):
    abc = abc + 1
    print(abc)
    if(abc == 13):
        continue
    if(abc == 15):
        break
        
output:
11
12
13
14
15

# 3

while(abc < 20):
    abc = abc + 1
    print(abc)
    if(abc == 13):
        continue
    if(abc == 15):
        break
        
output : 
      
11
12
13
14
15

# 4 

ghi = 5
for eachNumber in range(ghi):
    print('before while:',eachNumber)
    while(eachNumber < 25):
        print('inside while:',eachNumber)
        eachNumber = eachNumber + 20
    print('after while:',eachNumber)




  
  
