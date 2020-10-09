# #10 4
# import time


# test_cases=5

# steps=0  
# t1=time.time()
# def count(a,b):# 10 4
  
#   if a % b != 0: 
#      a+=1
#      global steps
#      steps+=1
#      count(a,b)
#      return 'TOTAL STEPS: {}'.format(steps)
#   else:
#      return 'TOTAL STEPS {}'.format(steps)
# t2=time.time()     


# a,b=int(input()),int(input())
# print(count(a,b))

# print(t2-t1)  

# poin=[10,20,30]
# a=[3,4,5]
#7,16,25
#4,12,20
#1,8,15
#
#

# print("yes zero is present" if 0 in poin else "cool")
# print("before",a)
# a=poin
# print("after",a)
# for i in range(len(poin)):
#     poin.pop()
# print(poin)	
point=[]
powerpuff = 0

def one_less(list1,list2):
    for i in range(len(list1)):
        if list1[i]<0:
            return True

def replace(list1,list2):
    for i in range(len(list2)):
        
        a=list1[i]-list2[i]
        point.insert(i,a)
        list1[i]=point[i]
    if one_less(list1,list2):
        pass
    else:
        global powerpuff
        powerpuff+=1
        replace(list1,list2)

    return powerpuff
    
  
        
       
  
       
        
        
       









   
        


