class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_hash = {}
        if len(nums)<=0:
            return 0
        i = 0
        man_nums=[]
        def prod_of_arr(nums):
            prod = nums[0]
            i=1
            while i < len(nums):
                prod = prod*nums[i]
                i+=1
            return prod
        while i < len(nums):
            man_nums=nums.copy()
            del man_nums[i]
            out_hash[i]=prod_of_arr(man_nums)
            i+=1
        return list(out_hash.values())
    