class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = list(sorted(set(nums)))
        if len(new_nums)<=0:
            return 0
        elif len(new_nums)==1:
            return 1
        candi_list = []
        candidate = []
        i=0
        while i+1<len(new_nums):
            if (new_nums[i+1]-new_nums[i])==1 and (new_nums[i] not in candidate):
                candidate.append(new_nums[i])
                candidate.append(new_nums[i+1])
            elif (new_nums[i+1]-new_nums[i])==1: 
                candidate.append(new_nums[i+1])
            elif len(candidate)!=0:
                candi_list.append(candidate)
                candidate=[]
            i+=1
            if i+1 == len(new_nums):
                candi_list.append(candidate)
        return len(sorted(candi_list,key=len,reverse=True)[0])