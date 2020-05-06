#1,2,3,5,8
# def fibo_even_sum(number):
#     if number<=0:
#         print("should enter correct input")
#     elif number==1:
#         return 0
#     elif number==2:
#         return 1    
#     else:
#         rem= fibo_even_sum(number-1) + fibo_even_sum(number-2) 
        
#         return rem   
# print(fibo_even_sum(3))      
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
sum=0

# check if the number of terms is valid
if nterms <= 0: 
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms: 
       #print(n1)
       if n1%2==0 and nterms>=n1:
           sum+=n1

       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1  
print("sum is",sum)