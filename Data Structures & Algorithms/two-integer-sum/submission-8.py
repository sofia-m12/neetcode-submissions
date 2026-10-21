class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indices!
        #nums has at least 2 elements, so return those if only 2
        #.extend() adds multiple elems to a list
        #start at idx: 0, 1 -> increment 1 to the end, then incrment 0 
        if(len(nums) == 2):
            return [0,1]
        result_list = []
        
        i = 0
        while(i < len(nums) - 1): #outer loop
            j = i+1
            while(j < len(nums)):
                if(nums[i] + nums[j] == target and i != j):
                    result_list.extend([i, j])
                    break
                j += 1
            i += 1
        return result_list