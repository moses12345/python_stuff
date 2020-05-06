matrix=[[1,2],   #00,01
        [3,4]]   #10,11
        #3,1     10 00
        #4,2     11 01
        #111   123
        #222   123
        #333   123

        #b=000 123
        #  000 123
#         #  000 123
# matrix=[[1,1,1],
#         [2,2,2],
#         [3,3,3]]       
# b=[[0,0,0],
#    [0,0,0],
#    [0,0,0]]        
# for i in range(3):
#     for j in range(3):
#         b[j][i]=matrix[i][j]

# print(b)
# def matrix_transponse(mat):
#     mat[0][1],mat[1][0]=mat[1][0],mat[0][1]
#     return mat
# print(matrix)
# print(matrix_transponse(matrix))

#cross word puzzle

# asml
# sdsf
# sxcd
#list of words to be find [ass,as,cd]
#first row
#second colum
#let begin 
words_list_to_be_find=['as','cd']
word_metrix=[['q','p','s','o'],
             ['s','a','s','f'],
             ['s','x','c','d']]
#for row wise
point_string=''
words=[]
for i in words_list_to_be_find:
    for lenght_ofword in range(len(i)):

                 for j in range(len(word_metrix)):
                     for inner in range(len(word_metrix)+1):

                            if i[lenght_ofword] == word_metrix[j][inner]:
                                #     global a
                                    point_string+=word_metrix[j][inner]
                                    words.append(point_string)
                                    break
                    break          
               
print(point_string)
print(words)


    