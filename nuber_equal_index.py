#[1,3,2,4] true
#[2,5,3] flase
list1=[1,0,2,4,5]
list2=[0,10,1,4,5]
list3=[5,9,0,1,2]

def indexing(listof):
    for i in range(len(listof)):
        if listof[i] == i:
            return list((i,True))
    else:
        return False  

# print(indexing(list1))  
# print(indexing(list2))  
print(indexing(list3))  

           