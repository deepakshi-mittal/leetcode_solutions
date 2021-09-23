class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        len_w = len(word)
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def backtrack(index, row, col):
            if index == len_w: 
                return True
            if row <0 or row ==m or col<0 or col ==n or board[row][col]!= word[index]:
                return False
            board[row][col] = "#"
            for dx, dy in directions:     
                if backtrack(index+1, row+dx, col+dy):
                    return True
            board[row][col] = word[index] # backtrack step
            return False
        
        for r in range(m):
            for c in range(n):
                if backtrack(0, r, c):
                    return True
        return False
