class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Approach 1 time - O(n), Space - O(1)
        count1, count2, ptC1, ptC2 = 0,0,None,None
        for num in nums:
            if num == ptC1:
                count1+=1
            elif num == ptC2:
                count2+=1
            elif count1 ==0:
                ptC1= num
                count1+=1
            elif count2==0:
                ptC2 =num
                count2+=1
            else:
                count1-=1
                count2-=1
                
        result = []
        # important step because it is not guranteed that majority element exists in array
        for candidate in [ptC1, ptC2]:
            if nums.count(candidate) > len(nums)//3:
                result.append(candidate)
        return result 

        # Approach 2 time - O(n), Space - O(n)
        # n = len(nums)
        # result =[]
        # counter = collections.Counter(nums)
        # for elem in counter:
        #     if counter[elem] > n//3:
        #         result.append(elem)
        # return result
