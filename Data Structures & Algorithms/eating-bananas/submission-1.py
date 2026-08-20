class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def _can_do(x):
            total_hours_taken=0
            for pile in piles:
                total_hours_taken+=math.ceil(pile/x)
            if total_hours_taken<=h:
                return True
            return False
        max_possible_k=max(piles)
        min_k_found_that_works=float('inf')
        left,right=1,max_possible_k
        while left<=right:
            mid=(left+right)//2
            if _can_do(mid):
                min_k_found_that_works=min(min_k_found_that_works,mid)
                right=mid-1
            else:
                left=mid+1
        return min_k_found_that_works