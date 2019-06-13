#-------------------------------------------------------------------------------
#    Valid Sodoku
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/valid-sudoku/
# Completed 6/13/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Sodoku:

    def __init__(self, board: [[str]]):
        self.board = board
        self.valid = True
        self.rows = [ set() for _ in range(9) ]
        self.cols = [ set() for _ in range(9) ]
        self.squares_key = {
            (0,0): 0,
            (0,1): 1,
            (0,2): 2,
            (1,0): 3,
            (1,1): 4,
            (1,2): 5,
            (2,0): 6,
            (2,1): 7,
            (2,2): 8
        }
        self.squares = [ set() for _ in range(9) ]
        self._validate()

    def _num_validate(self, num_str: str, row: int, col: int) -> bool:
        """Return True if :num_str: already exists in respective row, col and 
        square sets.
        """
        if num_str == '.':
            return False
        if num_str in self.rows[row]:
            return True
        elif num_str in self.cols[col]:
            return True
        elif num_str in self.squares[self.squares_key[(row//3, col//3)]]:
            return True
        return False

    def _insert(self, num_str: str, row: int, col: int) -> None:
        """Insert :num_str: into respective row, col and square sets."""
        self.rows[row].add(num_str)
        self.cols[col].add(num_str)
        self.squares[self.squares_key[(row//3, col//3)]].add(num_str)
        
    def _validate(self):
        """Insert numbers into rows, cols, and squares. :self.valid" updates to 
        False if duplicate entries occure.
        """
        for row in range(9):
            for col in range(9):
                num_str = self.board[row][col]
                if self._num_validate(num_str, row, col):
                    self.valid = False
                    return

                self._insert(num_str, row, col)    

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        """Return True if :board: represents a valid sodoku puzzle. This does 
        not guarantee a unique puzzle.

        Input:
        :board: [[str]] -> board number entries

        Output:
        bool -> True if board is valid
        """
        return Sodoku(board).valid

