#board
#dispaly board
#play game
#handle turns
#check win
 #check row
 #check coloum
 #check diagonal
#check tie
# flip palyers 
#_______________global variables_____________________

board=["-","-","-",
       "-","-","-",
       "-","-","-"]
game_is_goingon=True

winner=None

current_player="X"

def display_board():
  print("|"+ board[0] +"|"+ board[1]+ "|"+ board[2] +"|"+"             |"+"1  "+"2  "+"3 |")
  print("|"+ board[3] +"|"+ board[4]+ "|"+ board[5] +"|"+"             |"+"4  "+"5  "+"6 |")
  print("|"+ board[6] +"|"+ board[7]+ "|"+ board[8] +"|"+"             |"+"7  "+"8  "+"9 |")

  
def handle_turn(player):
  place=input("choose the postion from 1 to 9 :") 
  if place =="10":
    exit()
  try:
   place=int(place)-1
   if board[place]=="x":
     print("actually this place is occupied :]")
   else:
     board[place]="x"
  except ValueError:
    print("!!!!!!!!!! enter valid entry !!!!!!!!!!!") 
     
  
  display_board()
   


def play_game():
  #dispaly the board
  
  display_board()  
  while game_is_goingon:
    print("To exit game enter '10'")
    handle_turn(current_player)
    
 

    check_if_game_is_over()
    if check_if_game_is_over() != None:
      winner=check_if_game_is_over()
      break

    flip_palyer()
  if winner=="x" or "o":
    print(winner+" "+"won")  
  elif winner==None:
    print("tie")  

def check_if_game_is_over():
   
   #check rows
  if board[0] == board[1] == board[2]   =="x":
      winner = "x"
      return winner
  if board[3] == board[4] == board[5]  =="x": 
      winner = "x"
      return winner

  if board[6] == board[7] == board[8]  =="x":
      winner = "x"
      return winner
  #check column 
  if board[0] == board[3] == board[6]  =="x":
      winner = "x"
      return winner
  if board[1] == board[4] == board[7]  =="x": 
      winner = "x"
      return winner

  if board[2] == board[5] == board[8]  =="x":
      winner = "x"
      return winner 
  #diagonal    
  if board[0] == board[4] == board[8]  =="x":
      winner = "x"
      return winner 
  if board[2] == board[4] == board[6]  =="x":
      winner = "x"
      return winner         
  check_if_tie() 
  


  #check colum
  #check diagonal
   
def check_if_tie():
  return    
def flip_palyer():
  current_player="o"
  print("its 'o' turn")
  return current_player

     

  


play_game()