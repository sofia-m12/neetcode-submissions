class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: #if array was sotred n times(all the way around)
            return nums[0]
        # min element => 1st element that is < its previous
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

        