class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums, increasing order
        nums.sort()
        res = []
        n = len(nums)

        #iterate through nums, fixing i, for all possible positions of i
        for i in range(n-2):
            #stop if nums[i] is positive, sum wont ever be valid
            if nums[i] > 0:
                break
            
            #aovid duplicate i's
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # use 2 ptrs to find valid j, k
            j, k = i + 1, n - 1
            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k]
                
                if triple_sum < 0:
                    #increase the sum by moving j
                    j += 1
                elif triple_sum > 0:
                    #decrease the sum by moving k
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]]) #add the valid triplet
                    j += 1 #update both pointers
                    k -= 1

                    while j < k and nums[j] == nums[j-1]: #avoid using duplicates
                        j +=1
                        continue
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                        continue
        return res
        #TIME: O(N^2), outer loop is O(n), and the inner loop is O(n) worst case
        #Space: O(3m)= O(m), m is the number of triplets in the result array(3 is from triple)
        