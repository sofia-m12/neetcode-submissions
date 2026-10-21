from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can store list using a hashmap = (key anagram: list of strings that are anagrams)
        anagram_map = defaultdict(list)

        #how do we store all anagrams, need to use a COMMON key!
        # since anagrams have al same chars, and counts of them length are the same
        #so sorting the strings should yeoild the same string for each anagram


        #go thru str list
        for string in strs:
            #sort the currnet string,
            sorted_str = str(sorted(string)) #convert bc sorted returns a list
            #add the str to the list corresponding to the sorted version
            anagram_map[sorted_str].append(string)
        return list(anagram_map.values()) #return the lists(values in the map), as a list