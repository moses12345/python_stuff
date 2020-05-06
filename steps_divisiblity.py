#10 4
import time


test_cases=5

steps=0  
t1=time.time()
def count(a,b):# 10 4
  
  if a % b != 0: 
     a+=1
     global steps
     steps+=1
     count(a,b)
     return 'TOTAL STEPS: {}'.format(steps)
  else:
     return 'TOTAL STEPS {}'.format(steps)
t2=time.time()     


a,b=int(input()),int(input())
print(count(a,b))

print(t2-t1) 