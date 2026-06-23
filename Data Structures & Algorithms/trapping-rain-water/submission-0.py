class Solution:
    def trap(self, height: List[int]) -> int:
        total_water=0
        i=1
        while i<len(height)-1:
            curr_water=min(max(height[:i]),max(height[i+1:]))-height[i]
            if curr_water<=0:
                i+=1
            else:
                total_water+=curr_water
                i+=1
        return total_water