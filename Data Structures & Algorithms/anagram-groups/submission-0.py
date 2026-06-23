class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        analist={}
        for word in strs:
            if tuple(sorted((word))) in analist:
                analist[tuple(sorted((word)))].append(word)
            else:
                analist[tuple(sorted((word)))]=[word]
        return list(analist.values())