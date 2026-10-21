class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap {anagram: [anagrams list]}
        hmap = {}
        # .sort() order for each word, that would map each anagram to the same place
        
        #iterate thorugh strs
        for s in strs:
            hashv = "".join(sorted(s))
            if hashv in hmap: #if the list alr exists, add s to the end
                hmap[hashv].append(s)
            else:
                hmap[hashv] = [s] #else create the list
        
        # return all ,values() as a list 
        result = list(hmap.values())
        return result