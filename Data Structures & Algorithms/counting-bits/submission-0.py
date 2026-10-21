class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        offset = 1
        # loop through range(n + 1)
        for i in range(1, n+1):
            if i == (offset * 2): #check if current number is a power of two
                offset = i #set offset to the new power of two
            
            #add the count of 1's to result array
            output[i] = 1 + output[i - offset]
        return output

        #Time: O(n) -> jus tthe loop
        #Space: O(n) -> the output array stores n counts, one for each element, jus tvars otherwise

    #find a pattern in number of ones in consequetive numbers
        # 0, 1, 1, 2, 1, 2(5), 2(6), 3, 2

        # for num < 2^k, add 1 to the count of ones from 2^(k-1) positions before