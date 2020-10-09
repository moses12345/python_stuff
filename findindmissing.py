find=[1,5]
def finding(array):
    empty=[]
    for j in range(max(array)):
        if j+1 not in array:
            empty.append(j+1)
    return empty        

print(finding(find))    