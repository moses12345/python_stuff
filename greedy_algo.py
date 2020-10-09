 

denominations = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1

def returnChange(change, denominations):#30,
	# makes a list size of length denominations filled with 0
	toGiveBack = [0] * len(denominations)
   
   

	# goes backwards through denominations list
	# and also keeps track of the counter, pos.
	for pos, coin in enumerate(reversed(denominations)):
		# while we can still use coin, use it until we can't
		while coin <= change:
			change = change - coin
			toGiveBack[pos] += 1
	return(toGiveBack)
			
print(returnChange(30, denominations))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p
money=[1,5,10,30,40,50,100]
def changetobegiven(change1,money):
   tobereturn = [0]*len(money)

   for pos,coin in enumerate(reversed(money)):
      while coin <= change1:
         change1=change1-coin
         tobereturn[pos]+=1
   return(tobereturn)

print(changetobegiven(70,money))   
 

        


