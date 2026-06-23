class Solution:
    def isPalindrome(self, s: str) -> bool:
        betstring = ''.join(ch for ch in s.lower() if ch.isalnum())
        if len(betstring)==1:
            return True
        left = 0
        right = len(betstring)-1
        while left<right:
            if not betstring[left]==betstring[right]:
                return False
            left+=1
            right-=1
        return True