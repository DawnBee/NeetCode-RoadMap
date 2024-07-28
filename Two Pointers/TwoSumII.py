"""
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that 
they add up to a given target number target and index1 < index2. Note that 
index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
"""
from typing import List

# Using Two Pointers
def two_sum(nums: List[int], target: int) -> List[int]:
    # Two Pointer
    left, right = 0, len(nums)-1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]