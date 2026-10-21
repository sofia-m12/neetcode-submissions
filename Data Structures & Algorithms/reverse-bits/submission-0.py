class Solution:
    def reverseBits(self, n: int) -> int:
        #reverse bits = get the two's complement
        # flip bits, then negate
        # ~, -

        rev = 0
        # bit i -> bit 31 - i
        for i in range(32):
            b = (n >> i) & 1 #get ith bit
            rev += (b << (31-i)) #calculate decimal value of that bit(in reverse pistion)
            #add to total value of the reverse
    
        return rev