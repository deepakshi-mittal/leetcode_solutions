class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # Idea is Graph is given in n*n matrix representation already 
        # find number of new dfs start simiar to question 323
        # https://leetcode.com/problems/number-of-provinces/discuss/303150/python-union-find-dfs-bfs
        # print(isConnected)
        n = len(isConnected)        
        visited = set()
        def dfs(node):
            for index, connection in enumerate(isConnected[node]):
                if connection == 1 and index not in visited: # important condition
                    visited.add(index)
                    dfs(index)
        provinces = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                # increase province count everytime a new dfs is started
                provinces +=1
        return provinces
            
            
