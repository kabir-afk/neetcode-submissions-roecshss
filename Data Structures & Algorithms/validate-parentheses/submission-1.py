class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validBracket = {')':'(','}':'{',']':'['}
        for ch in s:
            if ch in validBracket:
                if stack and validBracket[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        print(stack)
        return True if not stack else False