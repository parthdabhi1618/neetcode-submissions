class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oprs={'+','*','/','-'}
        res=0
        for ch in tokens:
            if not ch in oprs:
                stack.append(int(ch))
            else:
                b=stack.pop()
                a=stack.pop()
                match ch:
                    case '+':
                        res=a+b
                    case '-': 
                        res=a-b
                    case '*':
                        res=a*b
                    case '/':
                        res=int(a/b)
                stack.append(res)
        return stack[-1]
                

            
