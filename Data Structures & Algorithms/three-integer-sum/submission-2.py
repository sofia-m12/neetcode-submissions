class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # THERE MAY NOT BE ANY TRIPLETS, initialize the output as an empty list
        #brute: 3 nested loops , O(n^3)
        #IS NUM SORTED? -> i should sort it
        nums.sort() #sort in place, O(n)
        res = []
        n = len(nums)

        for i in range(n - 2): #leave room for 2 other ptrs
            #set up j, k
            #stop if nums[i] is positive, sum wont ever be valid
            if nums[i] > 0:
                break
            
            #aovid duplicate i's
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k] #one calc
                #compare to 0, add to res
                if triple_sum < 0:
                    j += 1 #increase sum
                elif triple_sum > 0:
                    k -= 1 #decrease sum
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                #update ptrs
                    #no duplicate elements!!
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res
        #Time: O(n^2), nested loop
        #Space: O(3m), m is number of triplets in the reslt array, 3 is for triple
        