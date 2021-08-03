class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alphabet = {}
        i = 0
        for ch in order:
            alphabet[ch] = i
            i+=1
        # print(alphabet)
        n = len(words)
        for i in range(0, n-1):
        
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False # good hack here
                    # If words[i + 1] ends before words[i] and no different letters are found, then we need to                          return false because words[i + 1] should come before words[i] (for example, apple and app).
                if words[i][j] != words[i+1][j]:
                    if alphabet[words[i][j]] > alphabet[words[i+1][j]]:
                        return False
                    else:
                        break
                    
        return True
