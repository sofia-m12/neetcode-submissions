class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #claculating amount from max bar height * width
        #track max amount
        max_amount = 0

        #brute: nesdted loo,k check ee4ry bar combination, O(n^2)

        #alt:
        left, right = 0, len(heights) - 1
        #iterate thru heights, 2 ptrs, opposite end
        while left < right: #O(n)
            #cslculate the amount, compare to the m=current max 
            amount = min(heights[left], heights[right]) * (right - left)
            max_amount = max(max_amount, amount)
            #each loop, keep the max bar height, move the ptr of the shorter bar
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        #return final amount after itertation compelete
        return max_amount

        #Time: O(n), itertaion thru heights
        #Space: O(1), just variables and arithmetic
            
        