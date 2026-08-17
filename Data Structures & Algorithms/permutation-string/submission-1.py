class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left=0
        count=[0]*26
        
        for a,b in zip(s1,s2):
            count[ord(a)-ord('a')]+=1
            count[ord(b)-ord('a')]-=1
        
        if all(x==0 for x in count):
            return True
        
        for right in range(len(s1),len(s2)):
            count[ord(s2[left])-ord('a')]+=1
            count[ord(s2[right])-ord('a')]-=1
            left+=1
            if all(x==0 for x in count):
                return True
        
        return False
        