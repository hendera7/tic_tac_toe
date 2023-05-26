# tic_tac_toe
Simple tic-tac-toe game with 1-D array input



Playing a game of Tic-tac Toe is basically a 3x3 2-Dimensional array. The basic rules are that when 3 X's or O's are connected in a straight line, the X or O is declared the winner. If all spots are full and there are not three X’s or O’s in a straight line it is called a "CAT" game. If there is no winner and there are still empty spots, the game is considered "INCOMPLETE". 

 

If each spot in the Tic-toe game is identified as follows: 

0 | 1 | 2 

3 | 4 | 5 

6 | 7 | 8 

The input will look have corresponding spots of: [0,1,2,3,4,5,6,7,8]

For example, the following List: [X,O,O,-,X,O,-,-X] is the same as a tic tac toe game that looks like this: 

X | O | O

  | X | O 

  |   | X

And would result in 'X' being returned

The input Lists below will return the corresponding value: 

[X,O,O,-,X,O,-,-,X] Results in : X   
[O,O,O,-,X,O,-,X,X] Results in : O  
[-,O,O,-,X,O,-,-,X] Results in : INCOMPLETE   
[O,X,X,X,X,O,O,O,X] Results in : CAT
[,] or [A,B,C] or any other variations that are not only 'X','O' or '-' results in : INVALID 


Write a small program (python is preferred but not required) that given an input will return, INCOMPLETE, INVALID, CAT, X or O