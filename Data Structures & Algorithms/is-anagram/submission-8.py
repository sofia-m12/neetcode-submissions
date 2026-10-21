from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two coutner sets, one for each string, early check for same lenth
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
        
        #could also cut off some time(not alsways have to iterate thru both strings), by doing 1 Counter, then looping thru the other string and decrementing the counter values in the loop, catching non-anagrams earlier


        