class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # idea is to find if graph is fully connected , can have self loop or repeated edges
        # Node 0 works as root, keys in room i work as edge from room i to other rooms directed
        n = len(rooms)
        visited = [False for _ in range(n)]
        def dfs(node):
            for nei in rooms[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        visited[0] = True
        dfs(0)
        return all(visited)
