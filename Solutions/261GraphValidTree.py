class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # A graph is tree if a dfs algo is be covering all edges and no cycles
        if len(edges) != n-1:
            # we needed alteast n-1 edges to make a tree
            return False
        
    
        graph = [[] for _ in range(n)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        # print(graph)
        visited = [False for _ in range(n)]
        
        def dfs(node):
            if visited[node] == True:
                return False # loop
            visited[node] = True
            for each_nei in graph[node]:
                dfs(each_nei)
        dfs(0)
        if False in visited:
            return False
        return True
