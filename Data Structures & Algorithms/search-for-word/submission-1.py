class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtracking(row, col, index):
            if index == len(word):
                return True
    
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] != word[index]:
                return False
            
            # 1. Save what was there, so you can restore it later
            temp = board[row][col]

            # 2. Overwrite it with a sentinel value that can't match any real letter
            board[row][col] = '#'

            # 3. Now recurse — if the path loops back to this cell,
            #    board[row][col] != word[index] will be True (since it's '#'),
            #    so that path correctly fails instead of reusing the cell       
            found = (backtracking(row, col-1, index+1) or
                    backtracking(row, col+1, index+1) or
                    backtracking(row-1, col, index+1) or
                    backtracking(row+1, col, index+1))

            # 4. Restore the original value — "un-mark" it — 
            #    so cells outside this path (e.g. a different starting point, 
            #    or a sibling branch) can still use this cell normally
            board[row][col] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        
        return False
