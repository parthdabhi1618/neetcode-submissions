class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=0:
            return 0
        l=0
        h_table=dict()
        longest_sss=float("-inf")
        for r in range(len(s)):
            if not s[r] in h_table:
                h_table[s[r]]=1
            else:
                h_table[s[r]]+=1
            wind_size=r-l+1
            most_freq_char_in_window=h_table[max(h_table,key=h_table.get)]
            while not wind_size-most_freq_char_in_window<=k:
                h_table[s[l]]-=1
                l+=1
                most_freq_char_in_window=h_table[max(h_table,key=h_table.get)]
                wind_size=r-l+1
            longest_sss=max(longest_sss,r-l+1)
        return longest_sss