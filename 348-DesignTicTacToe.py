# Leetcode Design Tic-Tac-Toe
# Medium 1/11/21

# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

#     A move is guaranteed to be valid and is placed on an empty block.
#     Once a winning condition is reached, no more moves are allowed.
#     A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

# Implement the TicTacToe class:

#     TicTacToe(int n) Initializes the object the size of the board n.
#     int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

# Follow up:
# Could you do better than O(n2) per move() operation?

 

# Example 1:

# Input
# ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# Output
# [null, 0, 0, 0, 0, 0, 0, 1]

# Explanation
# TicTacToe ticTacToe = new TicTacToe(3);
# Assume that player 1 is "X" and player 2 is "O" in the board.
# ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|

 

# Constraints:

#     2 <= n <= 100
#     player is 1 or 2.
#     1 <= row, col <= n
#     (row, col) are unique for each different call to move.
#     At most n2 calls will be made to move.


# Solution 1
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.arr = [[-1 for i in range(n)] for j in range(n)]
        self.lim = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.arr[row][col] = player

        def check_diag(row,col):
            res = set()
            val = self.arr[row][col]
            cr = row
            cc = col

            while 0 <= cr < self.lim and 0 <= cc < self.lim:
                if val == self.arr[cr][cc]:
                    res.add((cr,cc))
                cr = cr - 1
                cc = cc - 1
            
            if len(res) == self.lim:
                return True
            
            res = set()
            cr = row
            cc = col

            while 0 <= cr < self.lim and 0 <= cc < self.lim:
                if val == self.arr[cr][cc]:
                    res.add
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# Solution 2

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.adiag = 0
        self.mp = {1:1, 2:-1}
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.rows[row]+=self.mp[player]
        self.cols[col]+=self.mp[player]      
        targets = [self.rows[row], self.cols[col]]
        if row==col:
            self.diag+=self.mp[player]
            targets.append(self.diag)
        if row+col==self.n-1:
            self.adiag+=self.mp[player]
            targets.append(self.adiag)

        for target in targets:
            if target == self.n: return 1
            if target == 0-self.n: return 2
        return 0


# T: O(a)
# S: O(a*b)
