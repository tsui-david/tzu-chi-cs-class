import numpy as np

def play(n, players):
    """Main function: 
       -- n should be the dimensions of the board (n x n)
       -- players should be a non-empty list of unique strings, serving
          as the symbol of each player.
          Typically, there are two players, but any number is supported.

       Creates a new board of size n x n and alternates between the given 
       players, prompting for moves until game is won or tied
      
       Returns None
    """

    # Create n x n game board
    board = initializeBoard(n)

    # Iterate over turns. Board has n*n cells, so there at most n*n turns.
    for turn in range(n*n): 

        # Select player by turn.
        player = players[turn % len(players)] 

        # Display board.
        print ('Current board (turn ' + str(turn) + '):')
        displayBoard(board)

        # Prompt player for a move.  Update the board.
        playMove(getValidMove(player, board), player, board)

        # Check for a win by player.
        if won(player, board):

            # Display winning player and final board
            print ('Player', player, 'wins!')
            displayBoard(board)
            return # Exit from loop early since game is done

    # Reaching here means the board is full after n*n moves,
    # but no player has won.
    print ('Game is tied.')
    displayBoard(board)
    return # Not necessary to say this, but indicates play function is done.

def initializeBoard(n):
  """Initializes the board with starting states, ie empty array
  -- n should be the dimension of the board (n x n)
  """
  return  #replace return with your code 

def displayBoard(board):
  """Prints out the board in console
  -- board is the 2d array of the state of the game
  
  Example:
  given: [['X', '', ''], ['X', 'O', '']['O', 'X', '']]
  
  X _ _
  X O _
  O X _
  """
  return  #replace return with your code 


def isValidMove(coordinates, board):
  """Checks whether the player has made a valid move
  -- coordinates is a tuple (row, coordinate)
  -- board is the 2d array of the state of the game
  """
  return # replace return with your code

def requestMove(player):
  """Asks input move from the player
  -- player is the current player doing the move
  """
  return  #replace return with your code


def getValidMove(player, board): 
  """Returns the valid move from the user.
  If not valid, asks the user for new move

  -- player is the current player doing the move
  -- board is the 2d array of the state of the game
  """
  return  #replace return with your code 

def playMove(move, player, board):
  """Changes the state of the game with the player move
  -- move is a valid move the player has entered
  -- player is the current player doing the move
  -- board is the 2d array of the state of the game
  """
  return  #replace return with your code 

def won(player, board):
  """Checks whether the current state of the game is a win
  -- player is the current player doing the move
  -- board is the 2d array of the state of the game
  """
  return  #replace return with your code 


# http://cs111.wellesley.edu/archive/cs111_spring17/public_html//psets/ps05/