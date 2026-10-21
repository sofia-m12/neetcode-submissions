class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # number XOR number = 0, duplicate cancel themsleves out
        # getting the XOR of all numbers in nums, will result in only having the sinlge number!
        
        res = 0 # a ^ 0 = a
        for n in nums:
            res = n ^ res
        return res