class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # variable to store the max
        #2 ptrs(vars) starting at each end to calculate the water that can be stored
        # while the ptrs dont overlap, calculate & compare to the max, then move the pointers

        # use the min height to calculate height - width

        max_water = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left #calculate distance from the indices

            #calculate current water storage
            # use min or else hte water will overflow
            curr_water = width * (min(heights[right], heights[left]))

            #compare to max
            max_water = max(max_water, curr_water)

            #update pointers(move the current smallest height)
            if heights[right] > heights[left]:
                left += 1#move the left
            else:
                right -= 1
        return max_water
        