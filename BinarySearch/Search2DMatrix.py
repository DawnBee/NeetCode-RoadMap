"""
*=Search 2D Matrix=*

You are given an m x n 2-D integer array matrix and an integer target.

* Each row in matrix is sorted in non-decreasing order.
* The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [
    [1,2,4,8],
    [10,11,12,13],
    [14,20,30,40]
]
target = 10
Output: true
"""
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2
            
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
    return False