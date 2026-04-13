class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        for row in matrix:
            end = len(row) - 1
            if target > row[-1]:
                continue
            else:
                # for num in row:
                #     if num == target:
                #         return True
                while start <= end:
                    mid = start + (end - start)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
        return False