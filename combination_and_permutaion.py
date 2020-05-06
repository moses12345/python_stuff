from itertools import permutations,combinations

perm=permutations([1,2,3],3)

for i in list(perm):
    print("this is permutation:",i)


combo=combinations([1,2,3],2)

for i in list(combo):
    print("this is combination",i)    