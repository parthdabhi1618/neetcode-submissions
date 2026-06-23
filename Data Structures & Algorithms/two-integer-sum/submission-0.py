class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        seen={}
        i=0
        for num in nums:
            if num in seen:
                return [seen[num][1],i]
            else:
                seen[target-num]=[num,i]
            i+=1
        return []
                