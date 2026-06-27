class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack=[]
            i=len(temperatures)-1
            res=[0]*len(temperatures)
            while i>=0:
                if (stack and stack[-1][0]>temperatures[i]):
                    res[i]=stack[-1][1]-i
                elif stack:
                    while stack and not stack[-1][0]>temperatures[i]:
                        stack.pop()
                    res[i]=stack[-1][1]-i if stack else 0
                stack.append((temperatures[i],i))
                i-=1
            return res

            



            