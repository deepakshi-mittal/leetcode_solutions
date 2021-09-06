class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # idea is to first make an adjacency list for undirected graph, then start dfs at each vertex while keeping a track of visited nodes. Every time a new dfs starts denote the number of connected components
        # Time Complexity - O(n*edges), Space - O(V)
        visited = [False]*n
        adj_list = [[] for _ in range(n)]
        # making the undirected adj list -  O(n)
       
        for source, destin in edges:
            adj_list[source].append(destin)
            adj_list[destin].append(source)
        
        # dfs function to mark all neighbours as visited
        def dfs(node):
            # -  O(edges)
            for adj_node in adj_list[node]:
                if visited[adj_node] == False:
                    visited[adj_node]  = True
                    dfs(adj_node)
                    
        connected_components = 0  
        # Time -  O(n)
        for node in range(n):
        
            if visited[node] == False:
                # this node will initiate a new dfs
                connected_components+=1
                visited[node]  = True
                dfs(node)
            
        return connected_components
