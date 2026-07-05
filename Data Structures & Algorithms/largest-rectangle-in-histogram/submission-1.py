class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        i=0
        max_area=0
        while i<len(heights):
            if not stack or heights[i]>heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and not heights[i]>heights[stack[-1]]:
                    top = stack.pop()
                    width=i-1-stack[-1] if stack else i
                    curr_area=heights[top]*width
                    if max_area<curr_area:
                        max_area=curr_area
                stack.append(i)
            i+=1
        while stack:
            top=stack.pop()
            width=len(heights)-1-stack[-1] if stack else len(heights)
            curr_area=heights[top]*width
            if curr_area>max_area:
                max_area=curr_area
        return max_area