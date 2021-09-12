class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # A very different approach - Good: Boyer-Moore Voting Algorithm - Idea is majority element cancels out all other elemnts n//2 +1 times so it remains candidate in end no matter what
        count =0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count -=1
        return candidate
      
        # n = len(nums)
        # counter = collections.Counter(nums)
        # for num in counter:
        #     if counter[num] > n//2:
        #         return num
        # return -1  
        
        # Approach 3 Sorting, given that the array has one Majority element 
        # n = len(nums)
        # nums.sort()
        # return nums[n//2]
      
