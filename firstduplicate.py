list1=[2,3,5,1,2,1,5,6,1,2]
def firstrelicate(list1):
    for i in range(len(list1)):
        if(list1[list1[i]-1]>0):
            list1[list1[i]-1]=-list1[list1[i]-1]
        else:    
            return list1[i]  
print(firstrelicate(list1))      


 