class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stk_i = stack.pop()
                res[stk_i] = i - stk_i
            stack.append(i)
        return res