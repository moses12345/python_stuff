import time
from functools import lru_cache

@lru_cache(maxsize=16)
def fib(n):
    if n ==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
t1=time.time()        
print([fib(x) for x in range(35)]) 
t2=time.time()    
print(t2-t1)
     
