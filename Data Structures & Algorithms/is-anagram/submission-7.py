from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two coutner sets, one for each string, early check for same lenth
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count



        