class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        if board is None:
            return [[]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if board[r][c] != "O":
                return 
            board[r][c] = 'S'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        # call dfs only start from border cells
        for i in range(row):
            dfs(i,0)
            dfs(i, col - 1)

        for j in range(col):
            dfs(0,j)
            dfs(row - 1, j)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        
        