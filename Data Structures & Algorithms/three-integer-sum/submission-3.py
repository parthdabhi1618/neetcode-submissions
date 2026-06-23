class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3:
            return []
        i = 0
        out_list = []
        nums=sorted(nums)
        while i<n-2:
            target = nums[i]*-1
            left, right = i+1,len(nums)-1
            if( i!=0 and nums[i]==nums[i-1]):
                i+=1
                continue
            while left<right:
                if nums[left]+nums[right]==target:
                    out_list.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
            i+=1
        return out_list