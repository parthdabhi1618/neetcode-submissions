class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=0:
            return 0
        l=0
        longest_l=0
        h_set=set()
        for r in range(len(s)):
            while s[r] in h_set:
                h_set.remove(s[l])
                l+=1
            h_set.add(s[r])
            longest_l=max(r-l+1,longest_l)
        return longest_l