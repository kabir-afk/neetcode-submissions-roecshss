class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            else:
                for num in row:
                    if num == target:
                        return True
        return False