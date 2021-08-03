class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        longest =0
        n = len(nums)

        current_num = float('-inf') # important to initialize
        current = 0 # important to initialize
        for e in hash_set:
            if e-1 not in hash_set:
                current_num = e 
                #### IMP updating current_num only when its teh first elements so while loop runs only a limited number of times, as current num will hold the max sequence's end value  from line 18, current_num +=1
                current =1
                
            while current_num+1 in hash_set:
                current_num +=1
                current +=1
            
            longest = max(current, longest)
        return longest
    
