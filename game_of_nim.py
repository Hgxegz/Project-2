from games import *
from utils import random_weights

random.seed("aima-python")
'''EXAMPLE TIC TAC TOE'''
'''
if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.play_game(alpha_beta_player, query_player)
    #ttt.play_game(alpha_beta_player, alpha_beta_player)
    #ttt.play_game(alpha_beta_player, random_player)
    #ttt.play_game(query_player, alpha_beta_player)

'''

class GameOfNim(Game):
    '''CONTRUCTOR TO INITIATE THE GAME'''
    def __init__(self, board):  
        #setting moves to an empty list that we will push tuples to
        moves = []
        for row in range(0, len(board)):
            for sticks in range(0, board[row]):
                moves.append((row, sticks+1))
        #setting the first player to move 
        to_move = 'Player 1'
        #setting the utility of the game(0 if no winner -> +1 = player 1 wins -> -1 = player 2 wins)
        utility = 0
        self.initial = GameState(to_move=to_move, utility=utility, board=board, moves=moves)
    '''COMPUTES THE MOVE TO THE CURRENT STATE AND RETURNS THE NEXT STATE'''
    def result(self, state, move):
        #row we will take the sticks from
        rowNumber = move[0]
        #number of sticks we will take
        numSticks = move[1]
        #now we take that away from the state.board
        board = state.board.copy()
        state.board[rowNumber] = state.board[rowNumber] - numSticks
        '''list of moves'''
        moves = []
        for row in range(0, len(state.board)):
            for sticks in range(0, state.board[row]):
                moves.append((row, sticks+1))
        return GameState(to_move=('Player 2' if state.to_move == 'Player 1' else 'Player 1'), 
                         utility=self.compute_utility(board,move,state.to_move), board=state.board, moves=moves)
    
    '''GIVEN OUR CURRENT STATE...RETURN THE LIST OF ACTIONS WE CAN DO'''
    def actions(self, state):
        return state.moves
    
    def terminal_test(self, state):
        if(sum(state.board) == 0):
            return True
        return False
    
    def utility(self, state, player):
        return state.utility if player == 'Player 1' else -state.utility

    def compute_utility(self,board,move,player):
        """If 'PLayer 1' wins with this move, return 1; if 'Player 2' wins return -1; else return 0"""
        row = move[0]
        sticks = move[1]
        board[row] = board[row]-sticks
        if(sum(board) == 0):
            return +1 if player == 'Player 1' else -1
        else:
            return 0

if __name__ == "__main__":
    board = [7,5,3,1]
    nim = GameOfNim(board)
    #utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    utility = nim.play_game(query_player, alpha_beta_player)
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
