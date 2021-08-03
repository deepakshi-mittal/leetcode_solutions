class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Neetcoe youtube , https://www.youtube.com/watch?v=6kTZYvNNyps
        adj_list = {c : set() for word in words for c in word}
        # print(adj_list)
        for i in range(len(words)-1):
            fw, sw = words[i], words[i+1]
            min_len = min(len(fw), len(sw))
            
            if len(fw) > len(sw) and fw[:min_len] == sw[:min_len]:
                return ""
            for j in range(min_len):
                if fw[j] != sw[j]:
                    adj_list[fw[j]].add(sw[j])
                    break
                    
        
        visited_map = {} # False = visited, True = its in current path
        output = []
        def post_order_dfs(node):
            if node in visited_map:
                return visited_map[node]
            visited_map[node] = True
            for next_node in adj_list[node]:
                if post_order_dfs(next_node):
                    return True
            visited_map[node] = False
            output.append(node)
    
        for node in adj_list:
            if post_order_dfs(node):
                return ""
        output.reverse()
        return "".join(output)
