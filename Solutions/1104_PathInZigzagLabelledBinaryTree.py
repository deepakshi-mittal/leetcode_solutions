class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        # Step 1: find level of label first
        # step 2: Travser to level 0 using formula label  = max_value -(cur_min)
        # parent = label /2
        level = 0
        node_at_level =1
        while( label >= node_at_level):
            level +=1
            node_at_level =node_at_level * 2
        result = []
        
        while(label!= 0):
            result.append(label)
            max_value = 2**level -1
            min_value = 2**(level-1)
            label = (max_value - label + min_value)//2
            level -=1
        # return in reverse order
        return result[::-1]
