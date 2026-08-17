class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2=len(s1),len(s2)
        left=0
        if l1>l2:
            return False
        char_h1=dict()
        char_h2=dict()
        for ch in s1:
            if ch not in char_h1:
                char_h1[ch]=1
                continue
            char_h1[ch]+=1
        for right in range(l1):
            if s2[right] not in char_h2:
                char_h2[s2[right]]=1
                continue
            char_h2[s2[right]]+=1
        if char_h1==char_h2:
            return True
        while right < len(s2)-1:
            if char_h2[s2[left]]>1:
                char_h2[s2[left]]-=1
            else:
                char_h2.pop(s2[left])
            left+=1
            right+=1
            if s2[right] not in char_h2:
                char_h2[s2[right]]=1
            else:
                char_h2[s2[right]]+=1
            if char_h1==char_h2:
                return True
        return False
            
