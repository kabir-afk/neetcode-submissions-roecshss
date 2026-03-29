class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenMap =  {')':'(','}':'{',']':'['}
        for ch in s:
            if ch in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False