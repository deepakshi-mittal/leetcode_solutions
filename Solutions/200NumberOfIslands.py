class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # using DFS
        # Idea: scan the 2d array, it a node contains one, increase the number of islands and triggger dfs from this node in 4 directions recursively, marking nodes as visited which encompass current island area.
        
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] =="1":
                    num_islands +=1
                    self.dfs(grid, r,c)
        return num_islands
        
    def dfs(self, grid, r, c)-> None:
        nr = len(grid)
        nc = len(grid[0])
        
        # return if outside Boundary or already visited or not part of island 
        if r <0 or c<0 or r>=nr or c >= nc or grid[r][c] =="0":
            return;
        
        grid[r][c] ='0' # marked visited
        
        self.dfs(grid, r, c-1) # left
        self.dfs(grid, r, c+1) # right
        self.dfs(grid, r-1, c) # top
        self.dfs(grid, r+1, c) # bottom
