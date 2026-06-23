class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        return [keys for keys,values in (sorted(freq.items(),key=lambda freq:freq[1],reverse=True)[:k])]
        