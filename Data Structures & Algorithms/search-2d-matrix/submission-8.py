class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        #find the critical point
        left=0
        right=rows-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][0]<=target:
                left+=1
            else:
                right-=1
        row=right
        #do binary search on the critical row
        left=0
        right=cols-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False
