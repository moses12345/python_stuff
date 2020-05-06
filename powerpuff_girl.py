#4 ingradients
#2,5,6,3 quantity to make a powerfu girl
#20,40,90,50 quantity of ingradients present in lab
from powerpuff2 import replace,point,powerpuff
import time
req_in=[2,3,10]
present_in=[10,20,30]

def count_powerpuff_girls(pre_in,req_in):
        return replace(pre_in,req_in)    

print("total number of powerpuff girls can be make from present ingredients present in lab are : ",count_powerpuff_girls(present_in,req_in))   
 

  
