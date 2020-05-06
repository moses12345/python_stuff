# 10  [3,5,6,9,10] sum= 33
suum=0

def sum(number):
    numbercount=0
    for i in range(3,number):
        if i%3 == 0 or i%5 == 0:
            global suum
            #global numbercount
            numbercount+=1
            suum+=i
    return 'sum of numbers are {} and total numbers between {} are {}'.format(suum,number,numbercount)  
print(sum(10))
