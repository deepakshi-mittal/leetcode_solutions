class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # https://www.youtube.com/watch?v=MGPHPadxhtQ&t=176s
        # count_l = min(countConZero, countConOnes)
        prevcount = 0
        curcount = 1 # whatever is at index 0 we incremnet its count by
        i = 1
        result = 0
        while i < len(s):
            
            if s[i] != s[i-1]:
                # means there is a switch from 1 to 0 or from 0 to 1
                
                result += min(prevcount, curcount)
                prevcount = curcount
                curcount = 1
            else:
                # //no change keep update current value's (can be 0 or 1 doesnt matter)
                curcount +=1
            i+=1
            
        return result + min(prevcount, curcount)
