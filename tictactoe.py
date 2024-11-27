# GAME PARAMETERS, EXPECTED OUTPUTS
# [X,O,O,-,X,O,-,-,X] Results in : X   
# [O,O,O,-,X,O,-,X,X] Results in : O  
# [-,O,O,-,X,O,-,-,X] Results in : INCOMPLETE   
# [O,X,X,X,X,O,O,O,X] Results in : CAT
# [,] or [A,B,C] or any other variations that are not only 'X','O' or '-' results in : INVALID 


# CHALLENGE INFORMATION:
# Start time: 7:35pm
# End time: 9:15pm
# Time building code: 55 minutes
# Time testing code: 45 minutes
# Total time on challenge: 1 hr 40 minutes

# RESOURCES CONSULTED:
# (1) https://www.w3schools.com/python/ref_func_filter.asp - information about the filter() method in Python (not used in the code)
# (2) https://stackoverflow.com/questions/12222706/check-if-list-contains-only-item-x  - information about how to check for "only __ items" in an array
# (3) https://codereview.stackexchange.com/questions/193004/python-tic-tac-toe-class - example of how to use classes for a 2-D tic-tac-toe game


# helper function
def valid(array):
    """
    The anticipated INPUT for this method is an array.
    This method will evaluate an array to make sure all values are either an "X", "O", or "-".
    """
    if len(array) < 9:  # if the array doesn't have 9 elements, it's invalid
        return False
    
    valid = True
    for i in range(0, len(array)-1):          
        # Only uppercase letters will be considered valid                  
        if array[i] == "X":
            valid = True
        elif array[i] == "O":
            valid = True
        elif array[i] == "-":
            valid = True
        else:
            valid = False
            return False
            
    return valid


# helper function
def winner(array):
    """
    The anticipated INPUT for this method is an array.
    This method will evaluate to see if the array values at specific indexes are the same to 
    determine if there is a winner.

    This method is a little long, and I researched other ways to do it, but everything 
    else involved a more complicated structure using classes. For the purpose of this
    challenge, I decided to keep it simple.
    """
    x_wins = False
    o_wins = False

    # checking for X wins
    if array[0] == "X" and array[1] == "X" and array[2] == "X":     # row 1 across win
        x_wins = True
    elif array[3] == "X" and array[4] == "X" and array[5] == "X":   # row 2 across win
        x_wins = True
    elif array[6] == "X" and array[7] == "X" and array[8] == "X":   # row 3 across win
        x_wins = True
    elif array[0] == "X" and array[3] == "X" and array[6] == "X":   # column 1 down win
        x_wins = True
    elif array[1] == "X" and array[4] == "X" and array[7] == "X":   # column 2 down win
        x_wins = True
    elif array[2] == "X" and array[5] == "X" and array[8] == "X":   # column 3 down win
        x_wins = True
    elif array[0] == "X" and array[4] == "X" and array[8] == "X":   # diagonal top left to bottom right win
        x_wins = True
    elif array[2] == "X" and array[4] == "X" and array[6] == "X":   # diagonal top right to bottom left win
        x_wins = True
    else:
        x_wins = False

    # checking for O wins
    if array[0] == "O" and array[1] == "O" and array[2] == "O":     # row 1 across win
        o_wins = True
    elif array[3] == "O" and array[4] == "O" and array[5] == "O":   # row 2 across win
        o_wins = True
    elif array[6] == "O" and array[7] == "O" and array[8] == "O":   # row 3 across win
        o_wins = True
    elif array[0] == "O" and array[3] == "O" and array[6] == "O":   # column 1 down win
        o_wins = True
    elif array[1] == "O" and array[4] == "O" and array[7] == "O":   # column 2 down win
        o_wins = True
    elif array[2] == "O" and array[5] == "O" and array[8] == "O":   # column 3 down win
        o_wins = True
    elif array[0] == "O" and array[4] == "O" and array[8] == "O":   # diagonal top left to bottom right win
        o_wins = True
    elif array[2] == "O" and array[4] == "O" and array[6] == "O":   # diagonal top right to bottom left win
        o_wins = True
    else:
        o_wins = False

    if x_wins == True and o_wins == True:   # if both X and O win, there is a rule violation, so no winner
        return False
    elif x_wins == True:
        return "X"
    elif o_wins == True:
        return "O"

    return False


# helper function
def incomplete(array):
    """
    The anticipated INPUT for this method is an array.
    This method will read the values of the array checking for any '-' values.
    """
    incomplete = False
    for i in range(len(array)):                  
        if array[i] == "-":
            incomplete = True
            return True
        else:
            incomplete = False
    
    return incomplete


# main function
def tictactoe(array):
    """
    The anticipated INPUT for this method is a 1D array with values at the indexes 
    corresponding to places in a tic-tac-toe game board (0-8).
    This method calls smaller helper methods for each possible outcome of the game. 
    This orgnizational choice was made for easier readability of the code.
    """
    if valid(array) == False:   # checks first to see if an entry is INVALID
        return "INVALID"
    if winner(array) != False:     # checks to see if there is a WINNER for the game
        return winner(array)
    elif incomplete(array) == True:     # if there is no winner, check to see if the game is INCOMPLETE
        return "INCOMPLETE"
    else:
        return "CAT"        # if a game is valid with no winner and is not incomplete, then it should be CAT




if __name__ == "__main__":

    # FULL PROGRAM TESTS
    test1 = [1, "n", "M"]                           # INVALID
    test2 = ["O","-","X",5,"-","-",2,"O","!"]       # INVALID
    test3 = ["-","O","-","-","-","O","X","X","X"]   # X WINS
    test4 = ["O","X","O","-","-","O","-","-","O"]   # O WINS
    test5 = ["X","X","X","-","-","O","O","O","O"]   # X AND O WIN (INCOMPLETE)
    test6 = ["-","X","X","X","X","O","O","O","X"]   # INCOMPLETE
    test7 = ["O","X","-","X","-","X","O","X","-"]   # INCOMPLETE
    test8 = ["O","X","X","X","X","O","O","O","X"]   # CAT
    test9 = ["X","O","O","O","O","X","X","X","O"]   # CAT
    # print(tictactoe(test9))


    # INVALID METHOD TESTS
    valid_test1 = ["O","X","X","X","X","O","O","O","X"]     # True
    valid_test2 = [1, "n", "M"]                             # False
    valid_test4 = ["O","-","X","-","-","-","O","O","X"]     # True
    valid_test5 = ["O","-","X",5,"-","-",2,"O","!"]         # False
    # print(valid(valid_test5))


    # WINNER METHOD TESTS
    winner_test1 = ["X","X","X","-","O","O","-","-","O"]
    winner_test2 = ["X","O","O","X","X","X","-","-","O"]
    winner_test3 = ["-","O","-","-","-","O","X","X","X"]
    winner_test4 = ["X","O","O","X","O","O","X","-","X"]
    winner_test5 = ["-","X","-","-","X","O","-","X","O"]
    winner_test6 = ["X","O","X","-","-","X","-","-","X"]
    winner_test7 = ["X","O","O","-","X","O","-","-","X"]
    winner_test8 = ["-","O","X","-","X","O","X","-","-"]

    winner_test9 = ["O","O","O","-","X","X","-","-","X"]
    winner_test10 = ["O","X","X","O","O","O","-","-","X"]
    winner_test11 = ["-","X","-","-","-","X","O","O","O"]
    winner_test12 = ["O","X","X","O","X","X","O","-","O"]
    winner_test13 = ["-","O","-","-","O","X","-","O","X"]
    winner_test14 = ["O","X","O","-","-","O","-","-","O"]
    winner_test15 = ["O","X","X","-","O","X","-","-","O"]
    winner_test16 = ["-","X","O","-","O","X","O","-","-"]
    # print(winner(winner_test1))


    # INCOMPLETE METHOD TESTS
    incomplete_test1 = ["O","X","X","X","X","O","O","O","X"]        # False
    incomplete_test2 = ["O","-","X","-","-","-","O","O","X"]        # True
    incomplete_test3 = ["O","X","X","X","X","O","O","X","-"]        # True
    incomplete_test4 = ["-","X","X","X","X","O","O","O","X"]        # True
    # print(incomplete(incomplete_test1))

