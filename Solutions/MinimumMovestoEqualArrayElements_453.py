class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        # Reverse engineer!  Math Problem can be thought of making all array elements equalt to the minimum element, whihc boils down to number of substractions( 1 each time) needed
        
        # n = len(nums)
        # min_value = float('inf')
        # sum_of_array = 0
        # for num in nums:
        #     sum_of_array +=num
        #     if num< min_value:
        #         min_value = num
        # return sum_of_array - n*min_value

        # Approach 2 Sorting
        # nums.sort()
        # moves = 0
        # for i in range(1, len(nums)):
        #     moves+= nums[i] -nums[0]
        # return moves
        
        # Approach 3 , calcualte on the fly, fastest
        n = len(nums)
        min_value = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_value
        return moves
        
