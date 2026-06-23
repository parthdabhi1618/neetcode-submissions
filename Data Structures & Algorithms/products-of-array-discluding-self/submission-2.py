class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<=0:
            return 0
        #forward pass
        forw=[1]*n
        prefix = 1
        for i in range(n):
            forw[i]=prefix
            prefix=nums[i]*prefix
        print(forw)
        #backword pass
        suffix=1
        while i>=0:
            forw[i]*=suffix
            suffix=nums[i]*suffix
            i-=1
        return forw