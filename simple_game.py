board = [None, None, None]
user1_selected_field = 0
user2_selected_field = 0

print("User1 is O, user2 is X. User1 starts.")
while True:
      key = input("make move")
      move = None
      if key == "a":
            move = "left"
      if key == "d":
            move = "rigth"
      if key == "":
           move = "enter"

      if move is None:
            print("Make move again")
            continue
      
      if move == "left":
            if user1_selected_field > 0: 
                user1_selected_field -= 1
            if user2_selected_field > 0: 
                user2_selected_field -= 1
      if move == "rigth":
            if user1_selected_field < 2: 
                user1_selected_field += 1
            if user2_selected_field < 2: 
                user2_selected_field += 1
    
      output = [" ", " ", " "]
      for i, board_move in enumerate(board):
           if board_move is not None:
             output[i] = board_move   

      len_board = len([board_move for board_move in board if board_move is not None])
      if len_board == 0 or len_board == 2: # If user1 turn
        if move == "enter":
          board[user1_selected_field] = output[user1_selected_field] = "O"
        else:
          output[user1_selected_field] = "-"
      else: # if user 2 turn
        if move == "enter":
          board[user2_selected_field] = output[user2_selected_field] = "X"
        else:
          output[user2_selected_field] = "_"
          
      print(" ".join(output))

      if len_board == 3:
          break
        
