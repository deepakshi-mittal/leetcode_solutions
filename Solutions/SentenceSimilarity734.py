class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        if len(similarPairs) ==0:
            return True
        spair = defaultdict(set)
        for (word1, word2) in similarPairs:
            spair[word1].add(word2)
            spair[word2].add(word1)
            
        # print(spair)
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 != word2 and word2 not in spair[word1]:
                return False
        return True
        
            
        
