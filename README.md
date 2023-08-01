# Intuition
The first thought to solve this problem is to understand the rules of Sudoku: 
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

We can loop through each cell in the board once and keep track of the digits seen in each row, each column, and each sub-box using a set. If we encounter a repeated digit in the same row, column, or sub-box, then it's not a valid Sudoku.

# Approach
The approach is to use three dictionaries to keep track of seen digits for each row, each column, and each sub-box respectively. We loop through each cell on the board, if it's not an empty cell, we check if we've seen this digit before in the current row, column, or sub-box. If we have, then it's not a valid Sudoku, we return False immediately. If we haven't, then we add this digit into the set for the current row, column, and sub-box. If we finished checking all cells without finding any repeated digits in the rows, columns, and sub-boxes, then it's a valid Sudoku, we return True.

# Complexity
- Time complexity: The time complexity is $$O(1)$$, because no matter how large the Sudoku puzzle, we're always dealing with 81 cells.
  
- Space complexity: The space complexity is also $$O(1)$$, because we're storing a constant amount of information - at most 81 entries across all our sets.

# Code
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sub_box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or \
                board[r][c] in col[c] or \
                board[r][c] in sub_box[(r//3, c//3)]:
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sub_box[(r//3, c//3)].add(board[r][c])
        
        return True
```
This Python code defines a `Solution` class with a method `isValidSudoku`, which takes a 2D list (board) and returns a boolean. This function utilizes the `defaultdict` class from the `collections` module and the `set` data structure to keep track of the numbers in each row, column, and sub-box.
