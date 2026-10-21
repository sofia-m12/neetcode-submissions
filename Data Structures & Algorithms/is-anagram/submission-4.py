class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # feed into stack(as a list), push each char
        # pop() 
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}
        for i in range(0, len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] += 1
            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1
        return hash_s == hash_t

        