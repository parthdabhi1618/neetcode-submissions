class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=[]
        for x in nums:
            if x in visited:
                return True
            visited.append(x)
        return False

