#input 2 3 5 1 4
#output 6 4
# 10                              
# 0 3 8 8 3 1 6 5 6 2 
# 20
# 82 98 70 21 88 16 30 77 97 82 35 44 73 50 29 4 68 53 73 55 
# 8
# 4 5 3 4 1 1 2 2 
# 20 9  338 206  6 6

entered=[]
even=0
odd=0
input1=input("total numbers : ")
for i in range(int(input1)):
    a=input("enter")
    entered.append(int(a))

for i in range(len(entered)):
    if i % 2==0:
        if entered[i] % 2==0:
            even=entered[i]+even
    else:
        if entered[i] % 2 != 0:
            odd=entered[i]+odd
print(even,odd)


    
    
    
 

  
       
        
        
       

